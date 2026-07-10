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

- [x] 新增通用镜头、电影灯光、电影色调和 film still 四个叶子
- [x] 更新 composition-camera、lighting-color 和 cinematic 索引
- [x] 创建 Phase 1 验证文档
- [x] 通用与专用路由可区分
- [x] 默认加载预算未突破

## Phase 2 执行记录

- [x] 更新发型、表情、微表情、单图输入和 Prompt 反推
- [x] 不新增重复妆容、基础 Prompt 和人物外貌万能页
- [x] 分离表情选择与自然发生机制
- [x] 分离单图输入与反推任务职责
- [x] 创建 Phase 2 验证文档

## Phase 3 执行记录

### 新增叶子

- [x] `references/controls/identity-consistency/character-identity-anchors.md`
- [x] `references/controls/spatial-blocking/staging-and-direction-control.md`
- [x] `references/libraries/composition-shot/storyboard-board-types.md`

### 更新 Playbook

- [x] `references/tasks/character-assets/playbook.md`
- [x] `references/tasks/scene-assets/playbook.md`
- [x] `references/tasks/storyboard-assets/playbook.md`

### 更新索引

- [x] identity-consistency
- [x] spatial-blocking
- [x] composition-shot

### 验证

- [x] 角色身份锚点与人物选项分离
- [x] 场景空间原点、三角站位和动线可执行
- [x] 控制型与风格型故事板边界清楚
- [x] 超过 12 镜优先拆分 Pack
- [x] 相邻单图任务不误加载资产控制叶子
- [x] 默认加载预算未突破
- [x] 创建 `docs/source-audits/user-curated-2026-07-10-phase-3-validation.md`
- [x] 更新 `references/SOURCES.md`

## 批次提交说明

当前 GitHub Contents 写入接口会按文件形成提交。后续具备 Git Tree / Commit API 时，优先让每个正式知识批次形成一个逻辑提交；如工具能力不支持，则在进度与验证文档中记录同批提交范围。

## 最近更新

- 2026-07-10：Phase 0 完成，建立来源治理、许可策略、验证模板和临时区隔离基线。
- 2026-07-10：Phase 1 完成，新增通用镜头、电影灯光、电影色调和电影画面语言四个叶子并接通路由。
- 2026-07-10：Phase 2 完成，增补发型、表情、微表情、单图输入和 Prompt 反推能力，并避免新增重复万能叶子。
- 2026-07-10：Phase 3 完成，补齐角色身份、空间调度、故事板类型和三类资产 Playbook。