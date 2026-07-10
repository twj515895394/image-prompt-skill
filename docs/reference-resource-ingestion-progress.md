# Image Prompt Skill 资源沉淀进度台账

## 用途

本文件跟踪 `docs/reference-resource-ingestion-implementation-plan.md` 的实际执行状态。

状态统一使用：

```text
待执行 / 进行中 / 已完成 / 阻塞 / 暂不采用
```

## 总体进度

| Phase | 内容 | 状态 | 主要产物或说明 |
|---|---|---|---|
| 0 | 来源治理与执行基线 | 已完成 | SOURCES、两份来源审计、验证模板、隔离验证 |
| 1 | 通用镜头、电影光影、电影画面语言 | 已完成 | 4 个基础叶子、4 个索引路由、批次验证 |
| 2 | 人物选择器、Prompt、参考图能力 | 已完成 | 5 个现有叶子增补；3 项重复候选不新建 |
| 3 | 角色、场景、分镜任务能力 | 待执行 | Playbook、controls 与必要 library 增补 |
| 4 | 写真、女友感、综合风格拆分 | 待执行 | 摄影风格增补与迁移结论 |
| 5 | 产品营销与电商主图 | 待执行 | awesome 首批 3–5 个高价值叶子 |
| 6 | 海报、文字和信息图 | 待执行 | 平面视觉、文字层级和版式知识 |
| 7 | 漫画、故事板与多格连续性 | 待执行 | 漫画风格、版式和连续性知识 |
| 8 | 摄影、电影、人物与场景交叉验证 | 待执行 | 验证并补强 Phase 1–4 |
| 9 | 插画、3D、游戏和长尾类别 | 条件启动 | 仅在真实需求与多案例支持下执行 |
| 10 | 自动检查、回归和临时区清理 | 待执行 | 检查脚本、回归报告、临时区清理 |

## Phase 0 执行记录

- [x] 建立 `references/SOURCES.md`
- [x] 建立两类来源审计和统一验证模板
- [x] 明确许可、署名和使用边界
- [x] 核对运行时入口未引用 `docs/source-staging/`
- [x] 创建 `docs/source-audits/phase-0-source-governance-validation.md`

## Phase 1 执行记录

### 新增叶子

- [x] `references/controls/composition-camera/shot-angle-lens-selection.md`
- [x] `references/controls/lighting-color/cinematic-lighting-patterns.md`
- [x] `references/libraries/lighting-color/cinematic-color-palettes.md`
- [x] `references/styles/cinematic/film-still-language.md`

### 更新索引

- [x] composition-camera
- [x] lighting-color control
- [x] lighting-color library
- [x] cinematic style

### 验证

- [x] 创建 `docs/source-audits/user-curated-2026-07-10-phase-1-validation.md`
- [x] 通用与专用镜头 / 光线路由可区分
- [x] 默认加载预算未突破

## Phase 2 执行记录

### 更新现有叶子

- [x] `references/libraries/human/hairstyle-selector.md`
- [x] `references/libraries/human/expression-selector.md`
- [x] `references/controls/pose-action/lifestyle-micro-expression.md`
- [x] `references/inputs/single-image-reference.md`
- [x] `references/tasks/prompt-reverse-engineering/playbook.md`

### 查重后不新增

- [x] 妆容选择器：现有叶子已完整覆盖
- [x] 基础 Prompt 结构：不建立第二套万能输出真源
- [x] 人物外貌万能页：选择器部分已有归属，写真风格延后 Phase 4

### 验证

- [x] 发型可独立命中，不默认加载妆容与表情
- [x] 表情选择与微表情发生机制分离
- [x] 静态终态与视频变化过程分离
- [x] 单图输入与反推任务职责分离
- [x] 风格变量与原图内容变量分离
- [x] 创建 `docs/source-audits/user-curated-2026-07-10-phase-2-validation.md`
- [x] 更新 `references/SOURCES.md`

## 批次提交说明

当前 GitHub Contents 写入接口会按文件形成提交。后续具备 Git Tree / Commit API 时，优先让每个正式知识批次形成一个逻辑提交；如工具能力不支持，则在进度与验证文档中记录同批提交范围。

## 最近更新

- 2026-07-10：Phase 0 完成，建立来源治理、许可策略、验证模板和临时区隔离基线。
- 2026-07-10：Phase 1 完成，新增通用镜头、电影灯光、电影色调和电影画面语言四个叶子并接通路由。
- 2026-07-10：Phase 2 完成，增补发型、表情、微表情、单图输入和 Prompt 反推能力，并避免新增重复万能叶子。