# 2026-11-21 GitHub VFX 特效构造资料审计

## 来源、许可与范围

- 来源名称：snowfrost/skill-movie 中的 vfx-effect-construction-engine 及其特效构造、家族分类、媒介整合参考。
- 来源 URL：https://github.com/snowfrost/skill-movie/tree/69f6db670ecf305e84f199e418bddbf2c1d988fe/vfx-effect-construction-engine
- 访问日期：2026-11-21；审阅修订：69f6db670ecf305e84f199e418bddbf2c1d988fe。
- 作者信息：GitHub 仓库所有者为 snowfrost；页面未提供可核实的其他署名要求。
- 许可证：GitHub 仓库 API 未声明许可证，根目录 LICENSE 文件不存在；具体许可状态未知。
- 资源规模：技能正文、多个分层参考、可检索双语 VFX 词汇库及检索脚本；词汇索引自述包含 566 条词条。
- 本次边界：用户指定为本地个人使用。项目仍仅以内部研究和结构抽象方式使用；不复制完整正文、词汇 JSON、代码或媒体资产。
- 抽样文件：`vfx-effect-construction-engine/SKILL.md`、`references/effect-construction-grammar.md`、`references/effect-family-atlas.md`、`references/medium-integration.md`、`references/vfx-atom-index.md`、`references/source-provenance.md`。
- 来源获取范围：抽样查看技能正文、特效因果语法、家族索引、静态图与视频分流、CG 媒介整合和词汇索引。未归档第三方原文或媒体。

## 查重与职责判断

现有 MJ 风格叶子负责 A–D 媒介判断、半写实 CG 表现、景深、面部柔化、散景与高光晕染；material-effect 目录此前只有分类索引，没有 VFX 正文。动画主视觉 style 中有少量特效和防遮挡要求，但范围限于动画 Key Visual；它不能代替模型无关的特效构造方法。不存在可更新的通用 VFX 构造叶子。

候选资料职责混合，按项目架构拆开：

| 候选知识 | 处理结果 | 原因 |
|---|---|---|
| 如何选主效果、确定静帧状态、构造来源到场景响应的可读关系 | 新增 control | 讲选择、组织与约束方法 |
| 能量、元素、弹体、武器轨迹、冲击、法术、召唤、转化、破坏、环境等视觉家族 | 新增 library | 提供具体类别、形态与材质选项 |
| 566 条双语原子词库和检索脚本 | 仅审计保留 | 对本项目的静态 Prompt 负载过大，不复制词库和工具；保留跨案例稳定的形态维度 |
| Seedance / Liu Prompt 结构、外部技能交接和视频生命周期 | 不采用 | 依赖原仓库工作流或超出本项目静态图片目标 |

## 正式沉淀

- Control：../../references/controls/effects/vfx-construction.md
- Library：../../references/libraries/material-effect/vfx-effect-families.md
- 路由：SKILL.md、对应任务 Playbook、controls/index.md、libraries/index.md、material-effect/index.md 与 MJ style 联动边界。
- 回归：github-vfx-effect-engine-2026-11-21-validation.md。
- 最终映射：github-vfx-effect-engine-2026-11-21-final-mapping.md。

MJ 风格继续作为单一 style 真源；VFX 家族库不会选择或复制 MJ 光学规则。单张图片冻结一个决定性时刻，不复述视频生命周期。
