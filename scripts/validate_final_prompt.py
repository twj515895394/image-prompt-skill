#!/usr/bin/env python3
"""Validate final image prompts against mechanically enforceable runtime rules.

This validator intentionally checks only rules that can be judged reliably from
text structure. Semantic checks such as identity fidelity, image-role correctness,
spatial coherence, and preservation of user locks remain the responsibility of
the Skill's Final Output Gate.

Examples:
    python scripts/validate_final_prompt.py --mode t2i --prompt "..."
    python scripts/validate_final_prompt.py --mode edit --generation-input-count 2 --prompt "..."
    python scripts/validate_final_prompt.py --mode edit --generation-input-count 1 --json-file result.json
    python scripts/validate_final_prompt.py --self-test
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BOOSTER_RE = re.compile(
    r"\b(masterpiece|award[- ]winning|highly detailed|ultra detailed|best quality|"
    r"photorealistic masterpiece|8k|4k|2k)\b",
    re.IGNORECASE,
)
RATIO_RE = re.compile(r"(?<!\d)\d{1,3}\s*:\s*\d{1,3}(?!\d)")
PIXEL_RE = re.compile(r"\b\d{3,5}\s*[x×]\s*\d{3,5}\b", re.IGNORECASE)
IMAGE_TAG_RE = re.compile(r"<image(\d+)>", re.IGNORECASE)
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
ASCII_LETTER_RE = re.compile(r"[A-Za-z]")
QUOTED_RE = re.compile(r'"[^"\n]*"')

IMPERATIVE_START_RE = re.compile(
    r"^\s*(?:please\s+)?(?:create|generate|make sure|ensure that|the ai should)\b",
    re.IGNORECASE,
)
SENTENCE_IMPERATIVE_RE = re.compile(
    r"(?:^|[.!?]\s+)(?:please\s+)?(?:create|generate|make sure|the ai should)\b",
    re.IGNORECASE,
)
MEDIUM_TERMS = (
    "photograph",
    "photo",
    "portrait",
    "poster",
    "illustration",
    "character sheet",
    "infographic",
    "3d render",
    "painting",
    "sketch",
    "cinematic still",
    "film still",
)
LIGHT_TERMS = (
    "light",
    "lighting",
    "sunlight",
    "daylight",
    "shadow",
    "highlight",
    "backlit",
    "rim light",
)


def strip_quoted_text(text: str) -> str:
    """Remove rendered-text literals before checking descriptive prose language."""
    return QUOTED_RE.sub("", text)


def validate_common_prompt(prompt: str) -> list[str]:
    errors: list[str] = []
    stripped = prompt.strip()
    if not stripped:
        return ["prompt is empty"]

    if "\n\n" in stripped:
        errors.append("prompt contains multiple paragraphs; canonical prompt should be one continuous paragraph")

    booster = BOOSTER_RE.search(stripped)
    if booster:
        errors.append(f"forbidden empty quality booster: {booster.group(0)}")

    ratio = RATIO_RE.search(stripped)
    if ratio:
        errors.append(f"numeric aspect ratio leaked into prompt body: {ratio.group(0)}")

    pixels = PIXEL_RE.search(stripped)
    if pixels:
        errors.append(f"pixel dimensions leaked into prompt body: {pixels.group(0)}")

    return errors


def validate_t2i(prompt: str) -> list[str]:
    errors = validate_common_prompt(prompt)
    stripped = prompt.strip()

    if IMPERATIVE_START_RE.search(stripped) or SENTENCE_IMPERATIVE_RE.search(stripped):
        errors.append("T2I prompt uses renderer-imperative language instead of observer prose")

    prose = strip_quoted_text(stripped)
    cjk_count = len(CJK_RE.findall(prose))
    latin_count = len(ASCII_LETTER_RE.findall(prose))
    if cjk_count > 8 and cjk_count > latin_count * 0.08:
        errors.append("T2I descriptive prose is not predominantly English")

    lowered = prose.lower()
    if not any(term in lowered for term in MEDIUM_TERMS):
        errors.append("T2I prompt does not clearly name a visual medium")

    if not any(term in lowered for term in LIGHT_TERMS):
        errors.append("T2I prompt does not contain an explicit lighting/shadow/highlight description")

    word_count = len(re.findall(r"\b[A-Za-z][A-Za-z'-]*\b", prose))
    if word_count < 30:
        errors.append("T2I prompt is too thin to reliably express the canonical observer description")

    if IMAGE_TAG_RE.search(stripped):
        errors.append("T2I prompt contains image tags even though final generation should not depend on image inputs")

    return errors


def validate_edit(prompt: str, generation_input_count: int) -> list[str]:
    errors = validate_common_prompt(prompt)
    stripped = prompt.strip()

    if generation_input_count < 1:
        errors.append("Edit mode requires at least one generation input")
        return errors

    tags = [int(value) for value in IMAGE_TAG_RE.findall(stripped)]

    if generation_input_count == 1:
        if tags:
            errors.append("single-generation-input Edit must use a natural image reference, not <image1>")
    else:
        expected = set(range(1, generation_input_count + 1))
        actual = set(tags)
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        if missing:
            errors.append(
                "multi-image Edit is missing required generation-input tag(s): "
                + ", ".join(f"<image{i}>" for i in missing)
            )
        if extra:
            errors.append(
                "Edit prompt references image tag(s) outside the generation-input map: "
                + ", ".join(f"<image{i}>" for i in extra)
            )

    return errors


def validate_qwen_payload(payload: object, mode: str, generation_input_count: int) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["structured payload must be a JSON object"]

    rewritten = payload.get("rewritten_prompt")
    if not isinstance(rewritten, str) or not rewritten.strip():
        return ["structured payload requires a non-empty rewritten_prompt string"]

    wh_ratio = payload.get("wh_ratio", "")
    ratio_follow = payload.get("ratio_follow", "")
    if not isinstance(wh_ratio, str) or not isinstance(ratio_follow, str):
        errors.append("wh_ratio and ratio_follow must be strings")
        return errors

    if wh_ratio and ratio_follow:
        errors.append("wh_ratio and ratio_follow are mutually exclusive")

    if mode == "t2i":
        if not wh_ratio:
            errors.append("Qwen T2I structured output requires wh_ratio")
        if ratio_follow:
            errors.append("Qwen T2I must not set ratio_follow")
        errors.extend(validate_t2i(rewritten))
    else:
        if not wh_ratio and not ratio_follow:
            errors.append("Qwen Edit structured output should set either wh_ratio or ratio_follow")
        if ratio_follow and not re.fullmatch(r"<image\d+>", ratio_follow):
            errors.append("ratio_follow must be an <imageX> tag")
        if ratio_follow and generation_input_count > 0:
            index = int(re.search(r"\d+", ratio_follow).group(0))
            if index > generation_input_count:
                errors.append("ratio_follow points outside the generation-input map")
        errors.extend(validate_edit(rewritten, generation_input_count))

    return errors


def load_prompt(args: argparse.Namespace) -> tuple[str | None, object | None]:
    if args.json_file:
        payload = json.loads(Path(args.json_file).read_text(encoding="utf-8"))
        return None, payload
    if args.prompt_file:
        return Path(args.prompt_file).read_text(encoding="utf-8"), None
    return args.prompt, None


def run_self_test() -> int:
    cases: list[tuple[str, list[str], bool]] = []

    valid_t2i = (
        "A vertical lifestyle photograph shows a young woman standing beneath a concrete pedestrian bridge in daylight, "
        "with modern office towers softly layered behind her. She stands near the center of the frame with a relaxed, "
        "balanced posture and a calm expression, wearing a short white ribbed cotton sports top and khaki trousers with "
        "natural fabric folds. Her skin retains subtle visible texture rather than a polished cosmetic finish. Soft daylight "
        "arrives from the upper left, creating gentle facial highlights and a grounded shadow beneath her body. The background "
        "remains naturally imperfect and slightly deep in focus, while the overall composition feels like an unedited rear-camera phone photograph."
    )
    cases.append(("valid_t2i", validate_t2i(valid_t2i), True))

    invalid_t2i = "Create a masterpiece 8K portrait in 9:16 with good lighting."
    cases.append(("invalid_t2i", validate_t2i(invalid_t2i), False))

    valid_edit_single = (
        "将图像中的人物上衣替换为短款白色罗纹棉运动背心，使腹部自然露出；保持人物身份、发型、姿态、构图、背景和其他未指定内容与输入图一致。"
    )
    cases.append(("valid_edit_single", validate_edit(valid_edit_single, 1), True))

    invalid_edit_single = "使用<image1>中的人物，仅修改上衣，其他保持不变。"
    cases.append(("invalid_edit_single", validate_edit(invalid_edit_single, 1), False))

    valid_edit_multi = (
        "以<image1>作为人物身份与主体画布，仅从<image2>提取服装结构并替换到<image1>人物身上；保持<image1>的人物身份、姿态、构图、背景和其他未指定内容一致，<image2>不提供脸部、体型或背景信息。"
    )
    cases.append(("valid_edit_multi", validate_edit(valid_edit_multi, 2), True))

    invalid_edit_multi = "保持<image1>人物身份并换装，背景不变。"
    cases.append(("invalid_edit_multi", validate_edit(invalid_edit_multi, 2), False))

    valid_json = {
        "rewritten_prompt": valid_t2i,
        "wh_ratio": "9:16",
    }
    cases.append(("valid_qwen_t2i_json", validate_qwen_payload(valid_json, "t2i", 0), True))

    failed = 0
    for name, errors, should_pass in cases:
        passed = not errors
        if passed != should_pass:
            failed += 1
            print(f"[FAIL] {name}: expected {'PASS' if should_pass else 'FAIL'}, got {'PASS' if passed else 'FAIL'}")
            for error in errors:
                print(f"       - {error}")
        else:
            print(f"[PASS] {name}")

    if failed:
        print(f"Self-test failed: {failed} case(s)")
        return 1

    print(f"Self-test passed: {len(cases)} case(s)")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate a final image prompt contract")
    parser.add_argument("--mode", choices=("t2i", "edit"), help="Finalizer mode")
    parser.add_argument("--prompt", help="Prompt string to validate")
    parser.add_argument("--prompt-file", help="UTF-8 text file containing the prompt")
    parser.add_argument("--json-file", help="Qwen-compatible structured JSON payload")
    parser.add_argument(
        "--generation-input-count",
        type=int,
        default=0,
        help="Number of images that will actually be passed to the generation model",
    )
    parser.add_argument("--self-test", action="store_true", help="Run built-in regression cases")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.self_test:
        return run_self_test()

    if not args.mode:
        parser.error("--mode is required unless --self-test is used")

    selected = sum(bool(value) for value in (args.prompt, args.prompt_file, args.json_file))
    if selected != 1:
        parser.error("provide exactly one of --prompt, --prompt-file, or --json-file")

    try:
        prompt, payload = load_prompt(args)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Validation failed: {exc}")
        return 1

    if payload is not None:
        errors = validate_qwen_payload(payload, args.mode, args.generation_input_count)
    elif args.mode == "t2i":
        errors = validate_t2i(prompt or "")
    else:
        errors = validate_edit(prompt or "", args.generation_input_count)

    if errors:
        print(f"Final prompt validation failed with {len(errors)} issue(s):")
        for index, error in enumerate(errors, 1):
            print(f"{index}. {error}")
        return 1

    print("Final prompt validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
