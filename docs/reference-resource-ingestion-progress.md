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
| 8 | 摄影、电影、人物与场景交叉验证 | 待执行 | 验证并补强 Phase 1–4 |
| 9 | 插画、3D、游戏和长尾类别 | 条件启动 | 仅在真实需求与多案例支持下执行 |
| 10 | 自动检查、回归和临时区清理 | 待执行 | 检查脚本、回归报告和临时区清理 |

## Phase 0–6 执行摘要

- [x] 建立来源治理、许可策略和验证基线
- [x] 完成用户整理资料 Phase 1–4 的迁移、去重与边界收敛
- [x] 完成产品营销与电商主图能力
- [x] 完成海报、文字与信息图能力

## Phase 7 执行记录

### 抽样与审计

- [x] 覆盖黑白日漫、彩色韩漫、条漫和美式动作漫画
- [x] 覆盖四格、对话页、动作页、故事板草稿和多格连续性
- [x] 覆盖对白框、旁白框、拟声词和跨格累计状态
- [x] 创建 `docs/source-audits/awesome-gpt-image-2-comic-storyboard-sampling.md`

### 新增正式叶子

- [x] `references/libraries/composition-shot/comic-panel-layouts.md`
- [x] `references/styles/comic-manhwa/sequential-comic-language.md`
- [x] `references/controls/identity-consistency/multi-panel-continuity.md`

### 更新

- [x] composition-shot index
- [x] comic-manhwa index
- [x] identity-consistency index
- [x] storyboard-assets Playbook

### 关键决策

- [x] 成品漫画页与制作型故事板明确分离
- [x] 四格并入漫画版式，不新增独立叶子
- [x] 对白与拟声词并入漫画视觉语言和图文层级
- [x] 多格连续性使用输入—变化—输出状态模型
- [x] 伤痕、道具损坏和服装破损作为累计状态
- [x] 单幅漫画插画不默认加载分格与多格连续性

### 验证

- [x] 黑白动作漫画、彩色条漫和四格短篇可正确命中
- [x] 制作型故事板不会默认加载漫画视觉语言
- [x] 道具、伤痕、位置和对白说话者可跨格继承
- [x] 默认加载预算未突破
- [x] 创建 `docs/source-audits/awesome-gpt-image-2-comic-storyboard-validation.md`
- [x] 更新 `references/SOURCES.md`

## 批次提交说明

当前 GitHub Contents 写入接口会按文件形成提交。各批次通过抽样、验证和进度文档记录逻辑提交范围。

## 最近更新

- 2026-07-10：Phase 0–4 完成用户资料迁移与边界收敛。
- 2026-07-10：Phase 5 完成产品营销与电商主图。
- 2026-07-10：Phase 6 完成海报、文字与信息图。
- 2026-07-10：Phase 7 完成漫画分格、漫画视觉语言、多格连续性和故事板边界补强。