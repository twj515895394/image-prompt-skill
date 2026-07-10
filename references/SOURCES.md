# Reference 来源登记

## 用途

本文件登记正式 Reference 所使用的外部或维护者提供资料，记录来源、许可、使用方式和对应正式文件。

它不参与运行时路由，不承载具体生图知识。

## 登记规则

每条来源至少记录来源名称、URL 或审计路径、日期、许可证或使用边界、使用方式、对应正式 Reference、直接引用情况和修改说明。

新增正式 Reference 或大幅更新现有叶子时，应同步更新本文件。

---

## 用户整理资料（2026-07-10）

- 来源名称：仓库维护者整理的生图知识资料，共 15 份 Markdown
- 临时位置：`../docs/source-staging/user-curated-2026-07-10/`
- 来源审计：`../docs/source-audits/user-curated-2026-07-10.md`
- 接收日期：2026-07-10
- 使用边界：由仓库维护者直接提供；第三方来源证据仍需逐项核实
- 使用方式：查重、结构提炼、规则改写、现有叶子增补和必要新叶子提炼
- 当前状态：Phase 1–4 已完成

### Phase 1

- `controls/composition-camera/shot-angle-lens-selection.md`
- `controls/lighting-color/cinematic-lighting-patterns.md`
- `libraries/lighting-color/cinematic-color-palettes.md`
- `styles/cinematic/film-still-language.md`

验证：`../docs/source-audits/user-curated-2026-07-10-phase-1-validation.md`

### Phase 2

- `libraries/human/hairstyle-selector.md`
- `libraries/human/expression-selector.md`
- `controls/pose-action/lifestyle-micro-expression.md`
- `inputs/single-image-reference.md`
- `tasks/prompt-reverse-engineering/playbook.md`

验证：`../docs/source-audits/user-curated-2026-07-10-phase-2-validation.md`

### Phase 3

- `controls/identity-consistency/character-identity-anchors.md`
- `controls/spatial-blocking/staging-and-direction-control.md`
- `libraries/composition-shot/storyboard-board-types.md`
- `tasks/character-assets/playbook.md`
- `tasks/scene-assets/playbook.md`
- `tasks/storyboard-assets/playbook.md`

验证：`../docs/source-audits/user-curated-2026-07-10-phase-3-validation.md`

### Phase 4

- `styles/photography/lifestyle-candid-photography.md`
- `styles/photography/index.md`

决策记录：`../docs/source-audits/user-curated-2026-07-10-phase-4-style-migration-decisions.md`

验证：`../docs/source-audits/user-curated-2026-07-10-phase-4-validation.md`

### 未形成新叶子的资料

- 妆容资料：现有正式叶子已覆盖；
- 基础 Prompt：由运行层、输入层、任务层和组装控制承担；
- 人物写真：由正交人物、镜头、光影和摄影风格组合承担；
- 综合生图风格选择器：只作为迁移来源。

## awesome-gpt-image-2

- 来源名称：Awesome GPT Image 2 Prompts
- 来源 URL：`https://github.com/YouMind-OpenLab/awesome-gpt-image-2`
- 来源审计：`../docs/source-audits/awesome-gpt-image-2.md`
- 访问日期：2026-07-10
- 许可证：CC BY 4.0
- 使用方式：分类抽样、案例拆解、结构提炼和规则抽象
- 直接引用策略：正式叶子不复制完整 Prompt、图片、具体品牌文案、对白或 IP 风格
- 当前状态：Phase 5–7 已完成，Phase 8–9 待处理

### Phase 5：产品营销与电商主图

抽样：`../docs/source-audits/awesome-gpt-image-2-product-commerce-sampling.md`

正式 Reference：

- `libraries/object-product/product-display-types.md`
- `controls/composition-camera/product-hero-composition.md`
- `controls/lighting-color/product-studio-lighting.md`
- `styles/photography/product-photography.md`
- `styles/3d-rendering/product-visualization.md`

验证：`../docs/source-audits/awesome-gpt-image-2-product-commerce-validation.md`

### Phase 6：海报、文字与信息图

抽样：`../docs/source-audits/awesome-gpt-image-2-poster-typography-infographic-sampling.md`

正式 Reference：

- `libraries/composition-shot/poster-layout-types.md`
- `styles/graphic-design/text-image-hierarchy.md`
- `styles/graphic-design/infographic-visual-language.md`

验证：`../docs/source-audits/awesome-gpt-image-2-poster-typography-infographic-validation.md`

### Phase 7：漫画、故事板与多格连续性

抽样：`../docs/source-audits/awesome-gpt-image-2-comic-storyboard-sampling.md`

正式 Reference：

- `libraries/composition-shot/comic-panel-layouts.md`
- `styles/comic-manhwa/sequential-comic-language.md`
- `controls/identity-consistency/multi-panel-continuity.md`
- `tasks/storyboard-assets/playbook.md`（边界增补）

验证：`../docs/source-audits/awesome-gpt-image-2-comic-storyboard-validation.md`

处理说明：漫画版式、漫画媒介表现和多格连续性分别沉淀；四格、对白与拟声词未建立重复独立叶子。

---

## 变更记录

- 2026-07-10：建立来源登记基线。
- 2026-07-10：完成用户资料 Phase 1–4 登记。
- 2026-07-10：完成 awesome Phase 5 产品视觉登记。
- 2026-07-10：完成 awesome Phase 6 图文设计登记。
- 2026-07-10：完成 awesome Phase 7 漫画、多格连续性与故事板边界登记。