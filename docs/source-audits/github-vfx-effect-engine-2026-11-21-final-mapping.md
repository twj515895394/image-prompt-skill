# GitHub VFX 特效构造参考最终映射

| 来源需求或知识职责 | 正式去向 | 说明 |
|---|---|---|
| 如何判断特效主次、冻结静帧状态并串联来源、形态、作用和环境响应 | `references/controls/effects/vfx-construction.md` | 唯一正式构造控制；模型无关，限制为单张图或静态关键帧 |
| 能量、元素、弹体、武器轨迹、冲击、法术、召唤、转化、破坏和环境效果 | `references/libraries/material-effect/vfx-effect-families.md` | 效果家族与可见形态库，不承载选择器正文 |
| 纯 MJ 景深、散景、柔化、晕染与电影光学效果 | `references/styles/cinematic/mj-atmospheric-film-look.md` | 现有 MJ 风格单一真源；不作为场内 VFX 路由 |
| 哪些任务按需读取 VFX 资料 | `SKILL.md`、`references/controls/index.md`、`references/libraries/material-effect/index.md`、相关任务 Playbook | 只记录条件与链接，不复制叶子正文 |
| 外部来源、修订、许可状态及取舍 | `references/SOURCES.md`、`docs/source-audits/github-vfx-effect-engine-2026-11-21.md` | 来源许可未知；按项目维护决策只保留内部抽象 |
| 正向、反向、静帧边界和加载预算验证 | `docs/source-audits/github-vfx-effect-engine-2026-11-21-validation.md`、`docs/reference-behavior-regression-final.md` Case 49–53 | 不声称执行过图像模型视觉验证 |

临时 `docs/source-staging/github-vfx-effect-engine-2026-11-21/` 仅保存本批来源定位和去向工作记录；正式映射、来源审计与验证均已保留后，按摄取流程清理临时目录。没有将第三方词库、脚本、媒体或完整技能正文复制进仓库。
