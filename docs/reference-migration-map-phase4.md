# Phase 4：现有 Reference 迁移映射

## 迁移原则

- 先建立新真源和新路由
- 验证内容完整后再删除旧文件
- 混合职责文件按内容拆分
- 同一知识只保留一个正文版本

## 第一批迁移映射

| 原文件 | 内容审计 | 新归属 | 处理方式 |
|---|---|---|---|
| `style-control/anti-ai-realism.md` | 真实感判断、拍摄来源、材质、构图瑕疵、负向建议 | `controls/realism-quality/anti-ai-realism.md` | 整体迁移并优化职责 |
| `style-control/candid-composition-imperfections.md` | 抓拍构图偏移、裁切、遮挡、通路机位 | `controls/composition-camera/candid-composition-imperfections.md` | 整体迁移 |
| `style-control/failure-patterns-negative.md` | 多领域失败模式和负向约束选择 | `diagnostics/common-image-failure-patterns.md` | 作为跨领域诊断迁移 |
| `scene-office/office-candid-photography.md` | 环境锚点、机位、混合光、摄影表现混合 | 见下方 4 个文件 | 按职责拆分 |
| `portrait/side-profile-bodyline.md` | 侧颜、体态、动作重心和镜头关系 | `controls/pose-action/side-profile-body-line.md` | 整体迁移并减少服装资料重复 |
| `portrait/commuter-outfit-bodyline.md` | 通勤单品、面料、版型和线条选择 | `libraries/human/commuter-outfit-materials.md` | 作为资料库迁移 |
| `portrait/lifestyle-micro-expression.md` | 微表情控制、视线、嘴角、肩颈和手部联动 | `controls/pose-action/lifestyle-micro-expression.md` | 作为表演控制迁移 |

## 办公室混合文件拆分

| 原内容 | 新文件 |
|---|---|
| 办公空间类型、道具和环境锚点 | `libraries/environment/office-workplace-environment.md` |
| 同事视角、侧后方、通路机位、构图关系 | `controls/composition-camera/office-candid-camera.md` |
| 顶灯、窗光、冷白反射和普通阴影 | `controls/lighting-color/office-mixed-light.md` |
| 生活化纪实摄影表现 | `styles/photography/lifestyle-candid-photography.md` |

## 暂不删除

第一批新文件和索引落地前，以下旧目录暂时保留：

- `references/style-control/`
- `references/scene-office/`
- `references/portrait/`

完成新路由检查后，再逐个删除已完成迁移的旧文件。

## 下一批

后续审计：

- `appendix/makeup.md`
- `appendix/hairstyle.md`
- `appendix/expression.md`
- 用户提供的《女主妆容选择器》
- 其余输入、模式和任务旧文件
