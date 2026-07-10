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
| 9 | 插画、3D、游戏和长尾类别 | 已完成 | 条件启动 4 项高价值能力，其余保留审计层 |
| 10 | 自动检查、回归和临时区清理 | 待执行 | 检查脚本、回归报告和临时区清理 |

## Phase 0–8 执行摘要

- [x] 建立来源治理、许可策略和验证基线
- [x] 完成用户整理资料 Phase 1–4 的迁移、去重与边界收敛
- [x] 完成产品营销与电商主图能力
- [x] 完成海报、文字与信息图能力
- [x] 完成漫画分格、漫画视觉语言和多格连续性能力
- [x] 完成摄影、电影、人物与场景交叉验证

## Phase 9 执行记录

### 启动判断

- [x] 用户历史请求中存在动画主视觉、角色资产、场景资产和游戏式视觉需求
- [x] 来源仓库和画廊存在多个不同案例支持
- [x] 候选方向可拆成媒介、透视、渲染和交付规则
- [x] 与现有产品、漫画、摄影和故事板叶子完成查重
- [x] 仅启动满足条件的方向

### 抽样与审计

- [x] Game Asset
- [x] Anime / Manga
- [x] Pixel Art
- [x] Isometric
- [x] Chibi / Q-Style 与 3D Render 作为辅助对照
- [x] 创建 `docs/source-audits/awesome-gpt-image-2-long-tail-game-illustration-sampling.md`

### 新增正式叶子

- [x] `references/libraries/composition-shot/game-asset-presentation-types.md`
- [x] `references/styles/anime/cinematic-anime-key-visual.md`
- [x] `references/styles/illustration/pixel-art-visual-language.md`
- [x] `references/styles/3d-rendering/isometric-miniature-world.md`

### 更新

- [x] composition-shot index
- [x] anime index
- [x] illustration index
- [x] 3d-rendering index
- [x] character-assets Playbook
- [x] scene-assets Playbook

### 关键决策

- [x] 游戏资产被定义为交付类型，不建立万能 game style
- [x] Key Visual 与角色 / 场景资产板明确分离
- [x] 像素艺术要求统一逻辑分辨率、像素簇和有限色板
- [x] 等距微缩世界要求功能区、连接结构和统一尺度
- [x] Chibi 不单独建 style，由比例、角色资产和 anime 组合承担
- [x] Cyberpunk 不单独建 style，由题材、光色、材质和现有媒介组合承担
- [x] Watercolor、Oil Painting、Sketch、Ink 和 App / Web Design 暂留审计层

### 验证

- [x] 游戏角色设定板、动画 Key Visual、Sprite、像素战斗和等距经营场景可正确命中
- [x] 普通动漫人物单图不误加载游戏资产交付类型
- [x] 普通真人场景资产不误加载像素、等距或动画 style
- [x] anime、pixel 和 isometric style 互斥选择
- [x] 默认加载预算未突破
- [x] 创建 `docs/source-audits/awesome-gpt-image-2-long-tail-game-illustration-validation.md`
- [x] 更新 `references/SOURCES.md`

## Phase 10 下一步

最低执行：

1. Markdown 相对链接存在性检查；
2. 索引目标路径检查；
3. 重复文件名和明显重复标题检查；
4. 正式 Reference 指向 `docs/source-staging/` 的违规检查；
5. 空叶子和只有标题文件检查；
6. 旧路径残留检查；
7. 扩展行为回归；
8. 清理临时摄取目录。

## 批次提交说明

当前 GitHub Contents 写入接口会按文件形成提交。各批次通过抽样、验证和进度文档记录逻辑提交范围。

## 最近更新

- 2026-07-10：Phase 0–4 完成用户资料迁移与边界收敛。
- 2026-07-10：Phase 5 完成产品营销与电商主图。
- 2026-07-10：Phase 6 完成海报、文字与信息图。
- 2026-07-10：Phase 7 完成漫画、多格连续性和故事板边界补强。
- 2026-07-10：Phase 8 完成摄影、电影、人物与场景交叉验证。
- 2026-07-10：Phase 9 条件启动并完成游戏资产交付、动画主视觉、像素艺术和等距微缩世界四项能力。