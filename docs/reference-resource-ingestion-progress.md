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
| 3 | 角色、场景、分镜任务能力 | 已完成 | 3 个新叶子、3 个 Playbook、3 个索引更新 |
| 4 | 写真、女友感、综合风格拆分 | 已完成 | 更新生活化纪实摄影；不新增 3 类重复万能页 |
| 5 | 产品营销与电商主图 | 已完成 | 5 个产品视觉叶子、5 个索引更新、抽样和验证 |
| 6 | 海报、文字和信息图 | 待执行 | 平面视觉、文字层级和版式知识 |
| 7 | 漫画、故事板与多格连续性 | 待执行 | 漫画风格、版式和连续性知识 |
| 8 | 摄影、电影、人物与场景交叉验证 | 待执行 | 验证并补强 Phase 1–4 |
| 9 | 插画、3D、游戏和长尾类别 | 条件启动 | 仅在真实需求与多案例支持下执行 |
| 10 | 自动检查、回归和临时区清理 | 待执行 | 检查脚本、回归报告、临时区清理 |

## Phase 0–4 执行摘要

- [x] 建立来源治理、许可策略、验证模板和临时区隔离基线
- [x] 补齐通用镜头、电影光影、电影色调和 film still
- [x] 增补发型、表情、微表情、单图输入和 Prompt 反推
- [x] 补齐角色身份、空间调度、故事板类型和三类资产 Playbook
- [x] 将亲近关系写真并入生活化纪实摄影唯一真源
- [x] 不建立妆容、基础 Prompt、人物写真和综合风格重复万能页

## Phase 5 执行记录

### 抽样与审计

- [x] 抽样 Product Marketing、E-commerce Main Image、Product、Food / Drink、Fashion Item
- [x] 覆盖极简悬浮、低角度美妆、手办、食品、饮料、巧克力、箱包和爆炸图
- [x] 创建 `docs/source-audits/awesome-gpt-image-2-product-commerce-sampling.md`
- [x] 记录作者、原始来源、CC BY 4.0 和改写方式

### 新增正式叶子

- [x] `references/libraries/object-product/product-display-types.md`
- [x] `references/controls/composition-camera/product-hero-composition.md`
- [x] `references/controls/lighting-color/product-studio-lighting.md`
- [x] `references/styles/photography/product-photography.md`
- [x] `references/styles/3d-rendering/product-visualization.md`

### 更新索引

- [x] object-product
- [x] composition-camera
- [x] lighting-color control
- [x] photography style
- [x] 3d-rendering style

### 验证

- [x] 白底电商、奢侈品美妆、动态饮料、食品广告可正确命中
- [x] 产品摄影与 3D 产品可视化路线可区分
- [x] 爆炸图和手办展示数量、结构与轴线可控制
- [x] 普通人物任务不误加载产品叶子
- [x] 默认加载预算未突破
- [x] 未修改 finished-image Playbook 和模板
- [x] 创建 `docs/source-audits/awesome-gpt-image-2-product-commerce-validation.md`
- [x] 更新 `references/SOURCES.md`

## 批次提交说明

当前 GitHub Contents 写入接口会按文件形成提交。后续具备 Git Tree / Commit API 时，优先让每个正式知识批次形成一个逻辑提交；如工具能力不支持，则在进度与验证文档中记录同批提交范围。

## 最近更新

- 2026-07-10：Phase 0–4 完成用户整理资料的正式迁移、去重与边界收敛。
- 2026-07-10：Phase 5 完成 `awesome-gpt-image-2` 产品营销与电商主图抽样，新增展示、构图、灯光、摄影和 3D 可视化五个叶子。