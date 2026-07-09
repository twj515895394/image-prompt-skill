# Image Prompt References Index

## 路由目标

用最少量 reference 完成最准确的当前任务。默认加载预算：

- `1` 份模式 reference
- `1` 份输入 reference
- `1` 份任务 reference
- `0-2` 份高价值控制 reference
- `0-2` 份附录

除非当前任务真的跨层，否则不要一次性加载多个任务 playbook。

## 路由优先级

当不同文件的建议看起来冲突时，按这个优先级执行：

1. 用户当前明确要求
2. 当前任务 playbook
3. 高频控制 reference
4. 输入分析 reference
5. 模式 reference
6. 附录

## 第一步：判断模式

### 快速模式

加载：

- `mode-quick/quick-mode.md`

触发信号：

- “直接给我 Prompt”
- “别问太多，直接出结果”
- 用户描述不长，但目标已经足够成型

### 交互模式

加载：

- `mode-interactive/interactive-mode.md`

触发信号：

- “先别直接出 Prompt”
- “先帮我一起定方向”
- “追问我”
- 用户明显在探索风格、人物气质或画面方向

## 第二步：判断输入

### 只有文字

加载：

- `input-text-only/text-expansion.md`

### 单张参考图

加载：

- `input-image-ref/image-reference-analysis.md`

### 多张参考图

加载：

- `input-image-ref/image-reference-analysis.md`

额外执行：

- 先判 `主参考图`
- 再给每张辅助图分配职责：妆容 / 发型 / 服装 / 光影 / 镜头 / 局部风格

## 第三步：判断任务

### 成片生图

加载：

- `task-finished-image/finished-image-playbook.md`

### 图生图

加载：

- `task-image-to-image/playbook.md`

### 角色资产

加载：

- `task-character-assets/character-assets-playbook.md`

### 场景资产

加载：

- `task-scene-assets/playbook.md`

### 分镜资产

加载：

- `task-storyboard-assets/playbook.md`

### 视频参考帧

加载：

- `task-video-reference-frames/playbook.md`

## 第四步：按需加载高价值控制页

### 高频控制页

以下文件不属于附录，而是“高价值控制 reference”。当用户明确要求真实感、抓拍感、漂亮侧颜、自然体态、办公室纪实时，优先于附录加载：

- `style-control/anti-ai-realism.md`
- `style-control/failure-patterns-negative.md`
- `style-control/candid-composition-imperfections.md`
- `portrait/side-profile-bodyline.md`
- `portrait/commuter-outfit-bodyline.md`
- `scene-office/office-candid-photography.md`
- `portrait/lifestyle-micro-expression.md`

推荐触发规则：

- 要“看不出 AI / 像真实照片 / 像手机拍的”：加载 `anti-ai-realism.md`
- 要“避免网红脸、塑料皮、假景深、伪抓拍”：加载 `failure-patterns-negative.md`
- 要“别太工整 / 像顺手拍到 / 有前景遮挡 / 有构图不完美”：加载 `candid-composition-imperfections.md`
- 要“漂亮侧颜 / 体态线条 / 弯腰、侧身、回头等姿态”：加载 `side-profile-bodyline.md`
- 要“通勤感 / 职场穿搭 / 靠衣服和面料带出线条”：加载 `commuter-outfit-bodyline.md`
- 要“办公室、茶水间、工位、会议室纪实抓拍”：加载 `office-candid-photography.md`
- 要“自然一点 / 别像面瘫 / 像活人 / 有生活化微表情”：加载 `lifestyle-micro-expression.md`

如果加载预算有限，优先顺序通常为：

1. `anti-ai-realism.md`
2. `failure-patterns-negative.md`
3. `candid-composition-imperfections.md`
4. 题材专项页（人物或场景）

## 第五步：按需加载附录

### 妆容附录

- `appendix/makeup-appendix.md`

在以下场景加载：

- 妆容直接决定人设
- 用户强调“白月光 / 港风 / 病娇 / 名媛 / 反派”等角色气质

### 发型附录

- `appendix/hairstyle-appendix.md`

在以下场景加载：

- 发型是一致性锚点
- 用户只说了“黑长直”“短发”“卷发”这种粗粒度词，需要细化

### 表情附录

- `appendix/expression-appendix.md`

在以下场景加载：

- 角色需要演出感
- 近景、特写、情绪镜头是重点
- 角色资产要出表情包或微表情组

## 第六步：必要时回查真源

如果当前任务对审美或题材控制要求很高，而现有 reference 仍不足以稳定结果：

- 只回查最相关的真源页
- 优先提炼高复用规则，再决定是否补写当前 skill
- 不把真源全文直接当作默认 reference 载入

## 任务选择提醒

- `成片生图` 重点是结果图完成度，不是资产复用。
- `角色资产` 重点是稳定锚点，不是氛围大片。
- `场景资产` 重点是空间、站位和动线，不是单张美图。
- `分镜资产` 重点是镜间承接，不是单镜极致细节。
- `视频参考帧` 重点是给后续运动留锚点，不是做普通海报。

## 禁止误用

- 不把附录当主文来跑完整任务
- 不把多个任务 playbook 叠在一起当“更全面”
- 不把主图和辅助图平均融合
- 不把“高价值控制页”误当成风格词列表，它们的职责是纠偏和控质
- 不把角色、场景、分镜、参考帧统称为“资产图”
