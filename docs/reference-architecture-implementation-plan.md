# Image Prompt Skill Reference 架构实施计划

## 1. 实施目标

在不一次性重写全部内容的前提下，将现有 Reference 体系迁移为已确认的新结构，并确保：

- Reference 按需加载
- Markdown 分级路由
- 默认三级、最多四级
- 多入口路由、单文件真源
- 方法规则、资料库、风格和诊断职责清晰
- 原有有效内容先迁移再删除
- 每个阶段都保持 Skill 可运行

---

## 2. 开发分支

```text
refactor/reference-architecture-v2
```

所有改造先在该分支完成，验证后再合并到 `main`。

---

## 3. 阶段划分

## Phase 1：运行骨架与输入层

目标：建立新架构主干，但暂不大规模删除旧文件。

实施内容：

1. 更新 `SKILL.md`
   - 保留快速模式与交互模式规则
   - 新增 8 类任务判断
   - 更新 Reference 加载顺序与预算
   - 删除对独立模式 Reference 的固定依赖
   - 明确 `controls / libraries / styles / diagnostics` 职责

2. 重写 `references/index.md`
   - 只做一级路由
   - 不承载详细知识
   - 路由到 `inputs / tasks / controls / libraries / styles / diagnostics`

3. 建立输入层新结构
   - `references/inputs/index.md`
   - `references/inputs/text-input-expansion.md`
   - `references/inputs/single-image-reference.md`
   - `references/inputs/multi-image-reference.md`

4. 旧输入文件暂时保留，待 Phase 4 完成迁移核对后删除。

验收标准：

- 纯文字、单图、多图请求能够明确三选一
- `SKILL.md` 不再要求读取模式 Reference
- 新总索引不直接展开所有叶子文件

---

## Phase 2：任务层补齐

目标：完成 8 类任务入口和任务边界。

实施内容：

1. 迁移现有任务 Playbook 到统一目录：
   - `finished-image`
   - `image-to-image`
   - `character-assets`
   - `scene-assets`
   - `storyboard-assets`
   - `video-reference-frames`

2. 新增：
   - `image-editing`
   - `prompt-reverse-engineering`

3. 建立 `references/tasks/index.md`

4. 明确：
   - 整体图生图与局部编辑边界
   - 反推 Prompt 的复现型、结构型、改造型路线
   - 产品图、海报、角色板等作为输出形态而非新增任务

验收标准：

- 每次任务只读取一个任务 Playbook
- 8 类任务不存在明显职责重叠
- 局部编辑具备完整编辑合同

---

## Phase 3：控制、资料库与风格主干

目标：建立可持续扩展的 Reference 主干。

实施内容：

1. 建立 8 个 `controls` 分类索引：
   - composition-camera
   - lighting-color
   - pose-action
   - spatial-blocking
   - identity-consistency
   - reference-handling
   - prompt-assembly
   - realism-quality

2. 建立 `libraries` 分类索引：
   - human
   - environment
   - object-product
   - animal-creature
   - composition-shot
   - lighting-color
   - material-effect

3. 建立 `styles` 分类索引：
   - photography
   - cinematic
   - anime
   - comic-manhwa
   - illustration
   - concept-art
   - 3d-rendering
   - graphic-design

4. 建立精简版 `diagnostics`。

5. 暂时只迁移现有最有价值内容，不为了填满目录创建空洞资料。

验收标准：

- 一级目录职责清晰
- 索引只写触发条件与路径
- controls 与 libraries 同领域不混淆

---

## Phase 4：现有 Reference 审计与迁移

目标：把原有内容迁入新结构并去重。

实施内容：

1. 制作迁移表：
   - 原文件
   - 有效内容
   - 新归属
   - 拆分或合并方式
   - 是否可删除旧文件

2. 优先迁移：
   - anti-ai-realism
   - failure-patterns-negative
   - candid-composition-imperfections
   - side-profile-bodyline
   - commuter-outfit-bodyline
   - office-candid-photography
   - lifestyle-micro-expression
   - makeup / hairstyle / expression appendix

3. 混合职责文件按内容拆分。

4. 新路由验证后再删除旧入口。

验收标准：

- 有效内容没有丢失
- 重复正文被消除
- 旧目录只在迁移完成后删除

---

## Phase 5：模板重构

目标：模板按任务划分，不再按快速/交互模式重复维护。

实施内容：

```text
assets/templates/
├── finished-image-template.md
├── image-to-image-template.md
├── image-editing-template.md
├── prompt-reverse-engineering-template.md
├── character-assets-template.md
├── scene-assets-template.md
├── storyboard-assets-template.md
└── video-reference-frames-template.md
```

验收标准：

- 模板只存输出结构
- 不重复任务知识
- 每次最多读取当前任务的一份模板

---

## Phase 6：最终清理与验证

实施内容：

1. 删除已完成迁移的旧目录：
   - mode-quick
   - mode-interactive
   - appendix
   - 旧任务目录和旧输入目录

2. 检查全部 Markdown 路径。

3. 检查同一正文是否存在多份。

4. 用典型请求验证路由：
   - 纯文字真人成片
   - 单图整体改写
   - 多图人物与服装组合
   - 局部物体替换
   - 角色资产板
   - 场景站位图
   - 故事板
   - 首尾帧
   - Prompt 反推
   - 失败诊断

验收标准：

- Skill 全流程可运行
- 默认加载不超过已确认预算
- 索引无死链
- 无重复真源

---

## 4. 默认加载预算

```text
固定：
- 1 份 input
- 1 份 task

按需：
- 0–2 份 controls
- 0–2 份 libraries
- 0–1 份 style
- 0–1 份 diagnostic
```

分类索引不计入业务 Reference 数量。

---

## 5. 当前开发范围

本轮先完成 Phase 1，并启动 Phase 2 的基础目录与索引。

不会在同一轮中直接删除旧 Reference，避免迁移未完成导致 Skill 失效。
