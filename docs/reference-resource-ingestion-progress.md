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
| 0 | 来源治理与执行基线 | 已完成 | SOURCES、来源审计、验证模板和隔离验证 |
| 1 | 通用镜头、电影光影、电影画面语言 | 已完成 | 4 个基础叶子和路由验证 |
| 2 | 人物选择器、Prompt、参考图能力 | 已完成 | 5 个现有叶子增补；重复候选不新建 |
| 3 | 角色、场景、分镜任务能力 | 已完成 | 身份、空间、故事板类型与 Playbook 增补 |
| 4 | 写真、女友感、综合风格拆分 | 已完成 | 更新生活化纪实摄影和迁移决策 |
| 5 | 产品营销与电商主图 | 已完成 | 5 个产品视觉叶子和验证 |
| 6 | 海报、文字和信息图 | 已完成 | 3 个图文设计叶子和验证 |
| 7 | 漫画、故事板与多格连续性 | 已完成 | 3 个漫画连续性叶子和故事板边界更新 |
| 8 | 摄影、电影、人物与场景交叉验证 | 已完成 | 新增环境人像；三条人物摄影路线边界收敛 |
| 9 | 插画、3D、游戏和长尾类别 | 待评估 | 仅在真实需求与多案例支持下启动 |
| 10 | 自动检查、回归和临时区清理 | 待执行 | 检查脚本、回归报告和临时区清理 |

## Phase 0–7 执行摘要

- [x] 建立来源治理、许可策略和验证基线
- [x] 完成用户整理资料 Phase 1–4 的迁移、去重与边界收敛
- [x] 完成产品营销与电商主图能力
- [x] 完成海报、文字与信息图能力
- [x] 完成漫画分格、漫画视觉语言和多格连续性能力

## Phase 8 执行记录

### 交叉验证范围

- [x] Photography、Portrait、Lifestyle、Cinematic
- [x] Environment、Character、Travel、Fashion Editorial
- [x] 对照 Phase 1–4 的摄影、电影、身份、空间和资产 Playbook

### 新增正式叶子

- [x] `references/styles/photography/environmental-editorial-portrait.md`

### 更新

- [x] `references/styles/photography/index.md`
- [x] `references/styles/photography/lifestyle-candid-photography.md`
- [x] `references/styles/cinematic/film-still-language.md`

### 关键结论

- [x] 生活化纪实：非摆拍、日常事件和关系视角
- [x] 环境编辑写真：适度摆姿、人物身份与地点关系
- [x] 电影剧照：剧情事件、关系变化和情绪落点
- [x] 三条路线按任务机制区分，不按“高级感”区分
- [x] 旅行、职业、城市街拍不建立题材型重复叶子
- [x] 角色身份与场景规划经验证后保持原结构
- [x] 不新增人物场景融合万能 control

### 审计与验证

- [x] 创建 `docs/source-audits/awesome-gpt-image-2-photography-cinematic-human-environment-cross-validation.md`
- [x] 创建 `docs/source-audits/awesome-gpt-image-2-photography-cinematic-human-environment-validation.md`
- [x] 伴侣生活照、旅行人像、职业肖像和剧情剧照路由可区分
- [x] 角色资产和场景资产不误加载摄影 style
- [x] 默认加载预算未突破
- [x] 更新 `references/SOURCES.md`

## Phase 9 启动条件

Phase 9 不自动全部执行。每个插画、3D、游戏或长尾类别需要同时满足：

1. 存在明确用户需求或高频任务；
2. 至少有多个不同案例支持；
3. 能拆成模型无关的线条、材质、渲染、透视或设计规则；
4. 与现有 styles 不重复；
5. 有清晰读取条件和回归样例。

## 批次提交说明

当前 GitHub Contents 写入接口会按文件形成提交。各批次通过抽样、验证和进度文档记录逻辑提交范围。

## 最近更新

- 2026-07-10：Phase 0–4 完成用户资料迁移与边界收敛。
- 2026-07-10：Phase 5 完成产品营销与电商主图。
- 2026-07-10：Phase 6 完成海报、文字与信息图。
- 2026-07-10：Phase 7 完成漫画、多格连续性和故事板边界补强。
- 2026-07-10：Phase 8 完成摄影、电影、人物与场景交叉验证，新增环境人像并收敛三条人物摄影路线。