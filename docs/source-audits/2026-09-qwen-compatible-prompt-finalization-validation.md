# 2026-09 Qwen-Compatible Prompt Finalization Validation

## 验证目标

验证新增 Prompt Finalization Contract 能在不破坏现有任务路由、Reference 加载预算和快速/交互模式合同的前提下，为最终 Prompt 增加统一的 Qwen-compatible 自然语言规范、QC 和自动修复。

## 正向回归

### Case 1：纯文字写实人物成片

输入：用户要求从零生成一张写实人物照片，给出服装、场景、构图和光线。

预期：

- 仍走 `text-input-expansion` + `finished-image`；
- 业务 Reference 路由不变；
- 最终阶段固定读取 `prompt-finalization-contract.md`；
- 最终 Prompt 为英文观察式自然语言描述，而不是命令式关键词列表；
- 用户明确颜色、服装、位置和构图保持不变；
- 输出前执行 QC，空泛 booster、重复和冲突自动修复；
- 快速模式只输出修复后的最终 Prompt。

### Case 2：单图局部换装

输入：用户要求只替换人物服装，脸、发型、姿势和背景不变。

预期：

- 仍走 `single-image-reference` + `image-editing`；
- Finalization 采用 Edit grammar；
- 只详细描述服装变化；
- 身份、发型、姿势和背景使用 blanket preservation，不重新逐项描脸；
- QC 检查 Attribute Leakage；
- 如果草稿错误重绘脸部，自动修复后再输出。

### Case 3：多图人物 + 服装 + 场景合成

输入：image1 提供人物身份，image2 提供服装，image3 提供场景。

预期：

- 仍走 `multi-image-reference`；
- 先建立唯一 Reference Role Map；
- 辅助图只提供指定维度；
- QC 检查身份污染和跨属性泄漏；
- Qwen 结构化请求时使用 `<image1>` 等显式标签；
- 非 Qwen 目标只替换表面引用语法，不改变角色职责。

### Case 4：角色设计图

输入：用户要求默认三分区写实真人角色设计图。

预期：

- 仍由 `character-assets` Playbook 决定三分区结构；
- `anti-ai-realism` 仍按现有条件加载；
- Finalization 不重新设计版式，只把既定三分区空间、人物身份、服装和光线整理成最终自然语言 Prompt；
- QC 检查三个区域职责、人物身份和可读性，不允许 Finalization 把三分区改成其他 Character Sheet 结构。

### Case 5：图片内指定文字

输入：用户明确要求海报标题为某一段中文原文。

预期：

- 最终 Prompt 中该文字逐字保留并使用直双引号包裹；
- 不翻译、不改标点、不自动补充副标题；
- QC 的 Text Literalness 能阻止错误改写。

### Case 6：Qwen API / JSON

输入：用户明确要求 Qwen-Image-2.1 API JSON。

预期：

- T2I 输出 `rewritten_prompt` + `wh_ratio`；
- Edit 输出 `rewritten_prompt` + `wh_ratio` + `ratio_follow`；
- `wh_ratio` 与 `ratio_follow` 互斥；
- 数字比例和分辨率不写入 `rewritten_prompt`；
- 不在结构化 payload 外重复一份 Prompt。

## 反向回归

### Case 7：普通快速模式不会显示 QC

输入：普通快速模式生图请求。

不应发生：

- 输出 QC 清单；
- 输出自动修复说明；
- 输出失败草稿；
- 输出多个候选方向；
- 因 QC 发现可内部修复的问题而向用户追问。

### Case 8：不为其他模型发明专属参数

输入：用户说“给 GPT Image 用”，但没有要求 API 参数。

不应发生：

- 自动输出 Qwen 的 `wh_ratio / ratio_follow` JSON；
- 凭空发明 GPT Image 私有字段；
- 改变已确定的视觉内容。

只复用通用最终 Prompt 语义骨架。

### Case 9：Finalization 不替代业务 Reference

输入：复杂角色、场景、海报或分镜任务。

不应发生：

- Finalization 自行选择新服装、场景或镜头；
- 跳过 task/input/control/library/style 路由；
- 为满足 Qwen 规范重写用户固定项。

## 加载预算验证

Prompt Finalization Contract 位于 `assets/templates/`，属于运行输出合同：

- 不增加 `0-2 controls` 配额占用；
- 不增加 `0-2 libraries` 配额占用；
- 不增加 `0-1 style` 配额占用；
- 不增加 `0-1 diagnostic` 配额占用。

业务 Reference 的原有加载预算保持不变。

## 模式合同验证

快速模式：

```text
零追问
+ 自动补全
+ Finalization
+ QC
+ 自动修复
+ 只输出最终 Prompt / Prompt Pack
```

交互模式：

```text
逐步设计阶段不强制 Finalization
→ 最终收口时 Finalization
→ QC
→ 自动修复
→ 最终交付
```

## 验收标准

- `SKILL.md` 固定路由到 Finalization Contract；
- 快速/交互模式输出合同都强制执行 Finalization + QC + 自动修复；
- source audit、SOURCES 和 final mapping 可追溯；
- `scripts/check_reference_integrity.py` 把新合同列为 required path；
- Reference Integrity CI 通过；
- 没有建立模型专属正式 Reference 目录；
- 没有复制 Qwen 官方完整 system prompt。
