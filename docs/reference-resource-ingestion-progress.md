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
| 0 | 来源治理与执行基线 | 进行中 | 已建立 SOURCES、两份来源审计、统一验证模板；待完成隔离核验记录 |
| 1 | 通用镜头、电影光影、电影画面语言 | 待执行 | 计划新增或增补 3–4 个基础叶子 |
| 2 | 人物选择器、Prompt、参考图能力 | 待执行 | 以更新现有叶子为主 |
| 3 | 角色、场景、分镜任务能力 | 待执行 | Playbook、controls 与必要 library 增补 |
| 4 | 写真、女友感、综合风格拆分 | 待执行 | 摄影风格增补与迁移结论 |
| 5 | 产品营销与电商主图 | 待执行 | awesome 首批 3–5 个高价值叶子 |
| 6 | 海报、文字和信息图 | 待执行 | 平面视觉、文字层级和版式知识 |
| 7 | 漫画、故事板与多格连续性 | 待执行 | 漫画风格、版式和连续性知识 |
| 8 | 摄影、电影、人物与场景交叉验证 | 待执行 | 验证并补强 Phase 1–4 |
| 9 | 插画、3D、游戏和长尾类别 | 条件启动 | 仅在真实需求与多案例支持下执行 |
| 10 | 自动检查、回归和临时区清理 | 待执行 | 检查脚本、回归报告、临时区清理 |

## Phase 0 执行记录

### 已完成

- [x] 创建 `references/SOURCES.md`
- [x] 创建 `docs/source-audits/user-curated-2026-07-10.md`
- [x] 创建 `docs/source-audits/awesome-gpt-image-2.md`
- [x] 创建 `docs/source-audits/validation-template.md`
- [x] 创建本进度台账
- [x] 明确用户资料和外部资源的许可、署名和使用边界
- [x] 明确正式 Reference 不得依赖临时摄取目录

### 待完成

- [ ] 核对 `SKILL.md` 与 `references/**/*.md` 不引用 `docs/source-staging/`
- [ ] 记录 Phase 0 验证结果
- [ ] 将 Phase 0 状态改为已完成

## 批次提交说明

当前 GitHub Contents 写入接口会按文件形成提交。后续具备 Git Tree / Commit API 时，优先让每个正式知识批次形成一个逻辑提交；如工具能力不支持，则在进度与验证文档中记录同批提交范围。

## 最近更新

- 2026-07-10：启动 Phase 0，完成来源登记、两类来源审计、验证模板和进度台账。