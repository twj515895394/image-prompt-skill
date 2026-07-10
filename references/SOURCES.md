# Reference 来源登记

## 用途

本文件登记正式 Reference 所使用的外部或维护者提供资料，记录来源、许可、使用方式和对应正式文件。

它不参与运行时路由，不承载具体生图知识。

## 登记规则

每条来源至少记录：

- 来源名称；
- 来源 URL 或仓库内审计路径；
- 访问或接收日期；
- 许可证或使用边界；
- 使用方式；
- 对应正式 Reference；
- 是否包含直接引用；
- 修改或抽象说明。

新增正式 Reference 或大幅更新现有叶子时，应同步更新本文件。

---

## 用户整理资料（2026-07-10）

- 来源名称：仓库维护者整理的生图知识资料，共 15 份 Markdown
- 临时位置：`../docs/source-staging/user-curated-2026-07-10/`
- 来源审计：`../docs/source-audits/user-curated-2026-07-10.md`
- 接收日期：2026-07-10
- 许可证或使用边界：由仓库维护者直接提供；原文中出现的第三方来源证据仍需逐项核实
- 使用方式：查重、结构提炼、规则改写、现有叶子增补、必要的新叶子提炼
- 直接引用策略：来源不清晰时不直接搬运完整案例或高度相似文案
- 修改说明：正式内容均经过拆分、重组和中文规则化表达，不把原始综合文件直接作为运行时叶子
- 当前状态：Phase 1–2 已完成，Phase 3–4 待处理

### Phase 1 对应正式 Reference

- `controls/composition-camera/shot-angle-lens-selection.md`
- `controls/lighting-color/cinematic-lighting-patterns.md`
- `libraries/lighting-color/cinematic-color-palettes.md`
- `styles/cinematic/film-still-language.md`

验证：`../docs/source-audits/user-curated-2026-07-10-phase-1-validation.md`

### Phase 2 对应正式 Reference

- `libraries/human/hairstyle-selector.md`
- `libraries/human/expression-selector.md`
- `controls/pose-action/lifestyle-micro-expression.md`
- `inputs/single-image-reference.md`
- `tasks/prompt-reverse-engineering/playbook.md`

验证：`../docs/source-audits/user-curated-2026-07-10-phase-2-validation.md`

### 已查重但未形成新叶子

- 女主妆容资料：现有 `libraries/human/female-makeup-selector.md` 已覆盖，无增量重写；
- 基础 Prompt 结构：由运行层、输入层、任务 Playbook 和 Prompt Assembly 共同承担，不新增万能页；
- 人物外貌与写真结构：可复用部分已由现有选择器承担，写真风格内容留待 Phase 4。

## awesome-gpt-image-2

- 来源名称：Awesome GPT Image 2 Prompts
- 来源 URL：`https://github.com/YouMind-OpenLab/awesome-gpt-image-2`
- 来源审计：`../docs/source-audits/awesome-gpt-image-2.md`
- 访问日期：2026-07-10
- 许可证：CC BY 4.0
- 作者与来源要求：社区投稿要求提供原作者和原始来源；直接引用或高度接近原文时必须保留署名
- 使用方式：分类抽样、案例拆解、结构提炼、规则抽象、少量必要引用
- 图片策略：不批量复制来源图片
- 模型策略：剥离 GPT Image 2 专属营销描述和偶然写法，优先沉淀模型无关的视觉规律
- 当前状态：待按实施计划 Phase 5–9 分批处理
- 对应正式 Reference：各批次完成后逐项补充

---

## 变更记录

- 2026-07-10：建立来源登记基线，登记用户整理资料和 `awesome-gpt-image-2`。
- 2026-07-10：登记用户资料 Phase 1–2 的正式 Reference、验证文档和未新增叶子结论。