# GitHub VFX 特效构造参考批次验证

## 验证目标

确认用户明确要求的场内 VFX 能进入静帧构造 control 与效果家族 library；MJ 光学效果仍进入现有 MJ style；图生图和局部编辑继续保留原图锚点；视频时序不会被单帧 VFX 叶子接管。

## 正向用例

### Case 1：MJ 半写实 CG 角色释放雷电

请求：生成一张 MJ 风格半写实 CG 人像，角色掌心凝聚雷电并沿手臂流动，局部照亮衣袖和雨夜背景。

预期：

- 输入：按实际输入读取文字或单图；任务：`finished-image/playbook.md`。
- 按需读取 MJ style、`controls/effects/vfx-construction.md` 与 `libraries/material-effect/vfx-effect-families.md`。
- MJ 负责主媒介和镜头光学；VFX 负责雷电来源、形态、作用路径及附近材质的局部响应。
- 保持 1 input + 1 task + 1 control + 1 library + 1 style，不重复加载光学规则。

结果：路由与职责审查通过；未运行图像模型，不声称已通过画面效果实测。

### Case 2：参考图中新增火焰

请求：在参考图人物手中增加火焰，保留人物身份、手势、服装、构图和室内场景。

预期：

- 输入：`single-image-reference.md`；任务：`image-to-image/playbook.md`。
- 只在授权范围新增火焰；VFX control 组织手部发射点、主轮廓、空间位置和衣袖或附近物体的局部受光。
- 不改动其余锚点，不将镜头散景误当作火焰粒子。

结果：路由与保留边界审查通过。

### Case 3：局部冲击特效编辑

请求：只为武器命中地面的区域增加冲击波、碎屑和尘土。

预期：

- 任务：`image-editing/playbook.md`；读取 VFX control 与家族 library。
- 限定编辑区域，表达命中中心、碎片或尘土方向、地面受力响应和主体可读性。
- 不把局部编辑扩展成全图重绘。

结果：路由与局部边界审查通过。

### Case 4：关键帧中的传送门

请求：生成一张角色跨入传送门的电影关键帧。

预期：

- 任务：`video-reference-frames/playbook.md`；VFX control 与家族 library 只描述当前静帧状态。
- 传送门有清楚的空间边界、前后遮挡和环境接触；不编写完整开门、穿越和关闭时间线。

结果：路由与静帧边界审查通过。

## 反向用例

### Case 5：MJ 只改镜头光学

请求：MJ 风格肖像，保留主体，只增加浅景深、暖冷散景和高光柔化。

预期：只读取 MJ style；不读取 VFX control/library，不增加法阵、能量、火花等场内对象。

结果：反向路由审查通过。

### Case 6：完整视频特效时序

请求：描述火焰从召唤、聚集、发射、命中到消散的连续过程。

预期：完整时间线由对应视频任务规则负责；VFX 叶子可按需帮助定义单张关键帧，但不取代时序、动作连续性或帧间状态规则。

结果：反向边界审查通过。

### Case 7：无明确特效的 CG 请求

请求：生成奇幻 3DCG 人像，没有要求法术、能量或攻击效果。

预期：只根据任务和风格路由；不因“奇幻”“CG”或“电影感”而加载 VFX library 或擅自添加特效。

结果：反向路由审查通过。

## 结构与预算检查

- Control 只说明如何取舍和组织，不重复列举家族正文。
- Library 只提供家族和可见形态，不复制 control 的步骤。
- 场内 VFX 与镜头光学分开：发光物体对场景的局部照明属于场内效果；景深、散景、镜头柔化与晕染属于风格层。
- MJ + VFX 同时命中时，固定加载 1 control + 1 library + 1 style，不超过默认预算。
- 快速模式仍只输出最终 Prompt；不展示 VFX 分析卡、维护说明或中间结构。
- 外部材料只做结构抽象；不复制词库、代码、媒体或完整正文。

## 验收结论

静态路由、职责、边界和加载预算审查通过；本地 `python scripts/check_reference_integrity.py`（151 个 Markdown、89 个 Reference、30 个路由索引）和 `git diff --check` 均通过，临时来源批次已清理。该验证不包含真实图像模型的视觉效果验证。GitHub Actions `Reference Integrity` 以合并前 PR 最新 Head 的结果为准。
