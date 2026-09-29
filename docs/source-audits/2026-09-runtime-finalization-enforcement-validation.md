# Runtime Finalization Enforcement Validation

## 目标

验证本轮重构解决的不是“文档有没有写规则”，而是实际运行时是否能稳定做出以下判断：

```text
Task Intent
→ Image Relevance / Role
→ Finalizer Route
→ Canonical Prompt
→ Final Output Gate
→ QC / Auto Repair
→ Output
```

## 关键回归

### 1. 纯文字 T2I

输入：只有文字，要求生成写实人物成片。

期望：

- input route = text；
- Finalizer = T2I；
- 英文 observer prose；
- 不使用 create / generate / make sure；
- 不使用 masterpiece / 8K / highly detailed；
- 数字画幅不进入 canonical prompt 正文。

### 2. 单图反推独立 Prompt

输入：一张照片，要求“分析并反推出以后可独立使用的 Prompt”。

期望：

- 图片 = ANALYSIS_SOURCE；
- Task = prompt-reverse-engineering；
- Finalizer = T2I；
- 最终 Prompt 不引用“这张图 / <image1>”。

### 3. 单图身份参考生成新角色板

输入：人物照片，要求“三分区角色设计图，五官保持一致”。

期望：

- 图片 = GENERATION_INPUT / identity；
- Task = character-assets；
- Finalizer = Edit；
- 单 generation input 不使用 `<image1>`；
- 身份绑定来源图，而不是重新详细描述五官。

### 4. 多图换装

输入：图 1 人物、图 2 服装，要求换装。

期望：

- 两张图都为 GENERATION_INPUT；
- Finalizer = Edit；
- `<image1>` = identity/canvas；
- `<image2>` = outfit only；
- 明确图 2 不提供脸、体型、背景；
- 防止跨属性污染。

### 5. 误带图片

输入：消息中有一张旧图片，但文字只要求“设计一个全新的赛博朋克城市夜景 Prompt”。

期望：

- 图片 = IRRELEVANT；
- input route = text；
- Finalizer = T2I；
- 最终 Prompt 不出现任何图片引用。

### 6. 图片只作上下文

输入：图片帮助解释概念，但用户明确说“不要参考这张图的视觉内容”。

期望：

- 图片 = CONTEXT_ONLY；
- 不建立 generation binding；
- 若没有其他 generation input，Finalizer = T2I。

### 7. 多图分析后产出通用模板

输入：多张海报，只要求比较共同版式并生成通用 Prompt 模板。

期望：

- 图片 = ANALYSIS_SOURCE；
- GENERATION_INPUT_COUNT = 0；
- Finalizer = T2I；
- 不生成 `<imageX>` 标签。

### 8. 单图局部编辑

输入：一张原图，要求仅修改上衣。

期望：

- 原图 = GENERATION_INPUT / canvas；
- Finalizer = Edit；
- 单图自然称“图像 / 图片中”；
- 不使用 `<image1>`；
- 只详细写上衣变化，其余使用 blanket preservation。

### 9. T2I Prompt Hygiene

候选 Prompt 包含：`Create a masterpiece 8K portrait in 9:16`。

期望：`scripts/validate_final_prompt.py` FAIL，至少命中：

- renderer imperative；
- booster；
- numeric ratio leakage；
- prompt too thin。

### 10. Edit 标签完整性

两张 generation inputs，但候选只引用 `<image1>`。

期望：validator FAIL，提示缺失 `<image2>`。

### 11. Qwen 结构化参数互斥

Edit JSON 同时设置 `wh_ratio` 与 `ratio_follow`。

期望：validator FAIL。

### 12. Task Playbook 不覆盖 Mode Contract

成片或反推 Playbook 包含内部分析字段时，快速模式不得输出：

- 画面概述；
- 主要约束；
- 自动补全项；
- QC 报告；
- Finalizer Route。

最终展示只服从 mode output contract。

## 自动验证

CI 执行：

```bash
python scripts/check_reference_integrity.py
python scripts/validate_final_prompt.py --self-test
```

`validate_final_prompt.py --self-test` 至少覆盖：

- valid T2I；
- invalid T2I；
- valid single-image Edit；
- invalid single-image tag；
- valid multi-image Edit；
- invalid missing multi-image tag；
- valid Qwen T2I JSON。

## 语义级人工验证

以下内容不能可靠由正则判断，仍必须由 Final Output Gate 做语义检查：

- 图片是否真的与用户当前提示词相关；
- ANALYSIS_SOURCE 与 GENERATION_INPUT 的区分；
- 身份是否漂移；
- 多图职责是否跨属性污染；
- User Lock 是否丢失；
- 空间、动作、光照、物理接触是否成立；
- Edit 是否发生未请求的重绘。

## 验收标准

```text
附件数量不再直接决定 Finalizer
+ 反推独立 Prompt 能稳定走 T2I
+ reference-conditioned generation 能稳定走 Edit
+ 无关图片不会污染 Prompt
+ Final Output Gate 位于 SKILL.md 主执行链
+ 可机械规则有真实 validator
+ CI 同时检查 Reference Integrity 与 Prompt Contract
+ 快速模式输出合同不被 Task Playbook 覆盖
```
