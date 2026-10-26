# 用户提供的通用服装设计图规范审计

## 来源

- 来源名称：用户在本对话中直接提供的通用服装设计图规范
- 来源方式：用户在本对话中直接提供文字；原文按 staging 验收流程临时保存，并在本批次完整性检查与 Reference Integrity CI 通过后清理。
- 接收日期：2026-10-26
- 许可与状态：用户直接提供；没有附带第三方图片、品牌、作者风格或外部文本。未引入或声称拥有任何第三方材料。
- 允许采用的方式：在本 Skill 中将要求抽象成通用、模型无关的任务规则。
- 禁止直接复制的内容：没有第三方内容需要复制；不得补写用户未提供的品牌、成分比例、工艺参数等事实。

## 资料判断

- 最终分类：`candidate-new-leaf`
- 核心职责：定义服装设计板任务的目标、输出结构、参考图职责、跨视角一致性和常见失败修复，归入 `tasks/`。
- 稳定读取条件：用户要求服装设计图、款式板、服装三视图或含细节和材质区域的 fashion design sheet。
- 案例范围：用户规范明确覆盖纯文字服装主题、服装参考图保真、不同衣物部件和材质、服装结构细节展示等场景；验证还包括相邻的人物身份板、时尚人像成片和局部换装编辑。

## 查重与边界

- `character-assets/playbook.md` 的主目标是锁定人物身份；真人脸与服装共同作为角色信息。新规范要求服装成为主焦点，模特去识别化，因此不能混为同一默认版式。
- `finished-image/playbook.md` 可处理时尚人像或品牌成片，但没有稳定约束三视图、细节样片和材质样片的资产版式。
- `libraries/object-product/product-display-types.md` 提到服装平铺，职责是选择产品展示类型，并不承担模特三视图与服装结构参考板。
- `libraries/human/commuter-outfit-materials.md` 只覆盖通勤服装和面料，不适合作为通用服装设计板的任务流程。
- 因此建立一个轻量 `fashion-design` task leaf；不新增面料库，不复制人物身份或产品摄影规则。

## 正式归属与路由

- 正式正文：`../../references/tasks/fashion-design/playbook.md`
- 路由：`../../references/tasks/index.md`、`../../references/index.md`、`../../SKILL.md`
- 加载预算：固定使用 1 input + 1 task；具体材质资料或复杂多图冲突时，才按需读取至多一个现有 library / control。
- 快速模式：沿用当前快速模式和 Prompt Finalization；最终单张设计板输出一份完整 Prompt，不展示任务分析。

## 正反向验证

验证用例和加载预算审查见 `user-curated-2026-10-26-fashion-design-sheet-validation.md`。本地完整性检查与 PR 最新 Head 的 Reference Integrity CI 均通过后，已按流程清理 staging 原文。
