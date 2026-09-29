---
name: image-prompt-skill
description: 当用户需要根据文字或参考图生成成片生图、整体图生图、局部图片编辑、参考图反推 Prompt、角色资产、场景资产、分镜资产或视频参考帧提示词时，应使用此技能。
---

# Image Prompt Skill

## 使用目标

把用户的创作意图转成可直接投喂生图模型的完整 Prompt，而不是只给灵感词或风格清单。

默认目标是：

- 快速模式直接输出可复制的最终 Prompt 或 Prompt Pack；
- 交互模式先完成必要设计决策，再输出结构化最终结果；
- 主体、场景、动作、镜头、光影、材质、风格和限制必须形成同一套可执行描述；
- 最终 Prompt 在对外输出前必须经过统一 Prompt Finalization、Final Output Gate、QC、自动修复和 QC 复检。

## 适用范围

支持以下任务：

- 成片生图
- 整体图生图改写
- 局部图片编辑
- 参考图反推 Prompt
- 角色资产
- 场景资产
- 分镜资产
- 视频首帧、尾帧和关键帧

不负责：

- 视频时间轴拆解
- 以运镜和时序为核心的完整视频 Prompt
- 视频下载、抽帧或文件解析

## 核心原则

- 除非用户明确要求讨论、脑暴、逐步设计或先提问，否则默认进入快速模式。
- 快速模式零追问、零人工确认、零过程说明，直接输出可用 Prompt。
- 交互模式遵循 `grill-me`：每次只问一个最关键的问题，并给出推荐答案。
- 不把用户拉去填长表；能从文字、图片和上下文推断的内容直接推断。
- 静态图片需要写实或去 AI 感时，按“结构与因果 → 镜头与光线 → 材质 → 语境中的合理不完美”检查；不要把瑕疵、颗粒或质量词当成写实开关。
- 静态图片的细节密度服从景别与观看距离；任务语境决定理想化程度，商业产品、商业人像和写实 CGI 不自动套用生活纪实瑕疵。
- 不用“高级感、电影感、氛围感”代替可执行的镜头、光影、色彩、材质和情绪描述。
- Reference 可以很多，但每次只读取当前任务真正需要的一条或几条路线。
- 同一知识只保留一个正文真源；不同索引可以指向它，但禁止复制正文。
- 不向用户暴露内部目录、维护路径和知识迁移过程。
- 视觉设计由 Task / Input / Controls / Libraries / Styles 决定；最终表达由 `assets/templates/prompt-finalization-contract.md` 统一规范，模型规范层不得反向覆盖已经确定的视觉意图。
- 默认最终表达以 Qwen-Image-2.1 Prompt Enhancer 的核心语法作为 canonical grammar；GPT Image、Nano Banana 等模型只能做最小表面适配，不得借“跨模型兼容”放宽 canonical hard rules。
- **附件数量不决定 T2I / Edit。最终表达模式由“最终生成时是否仍依赖输入图片”决定。**

## 第一步：判断任务

优先根据用户当前提示词的语义判断任务，只读取一份任务 Playbook。附件存在与否不能覆盖任务语义。

### 1. 成片生图 `finished-image`

生成一张高完成度结果图。产品图、海报、封面、写真、概念图等属于它的输出形态。

### 2. 整体图生图 `image-to-image`

保留部分参考锚点，对构图、场景、服装、光影、色调或风格进行整体改写。

### 3. 局部图片编辑 `image-editing`

只修改指定对象、区域、文字、动作或细节，并明确其他内容保持不变。

也包括：对已有成片做保真细节增强，只补皮肤微观纹理或有效分辨率。这类请求属于局部编辑，不属于整体图生图，也不应重新抽卡。

### 4. 参考图反推 Prompt `prompt-reverse-engineering`

根据用户意图选择：

- 复现型：尽量还原原图；
- 结构型：提炼可复用视觉公式和模板；
- 改造型：继承原图部分信息并生成新目标 Prompt。

反推任务中的图片通常是 `ANALYSIS_SOURCE`，不能因为附件存在就自动把最终 Prompt 判成 Edit。若最终结果要脱离原图独立生成，Finalizer 走 T2I；只有最终生成仍要把原图作为模型输入时才走 Edit。

### 5. 角色资产 `character-assets`

生成三视图、多角度头像、表情板、换装板、手部、鞋履和角色主视觉等可复用资产。

当用户使用“角色设计图”“角色参考图”或“character sheet”等泛称，且未指定其他版式时，按 `references/tasks/character-assets/playbook.md` 中的默认三分区版式执行：正面身体、背面身体、以及一个正常表情的人脸特写。若用户提供人物参考图，并说“参照图中人物特征生成一张角色图 / 人物角色图”，同时没有要求场景、动作、海报、宣传图或主视觉，也按这一默认三分区版式执行，不要求用户必须说出“角色设计图”。正面身体区去掉头部，背面身体区保留后脑但不露脸；人脸区只放一个正常表情，不再在同一张图里并排或上下放置多个表情。用户需要微笑、左转 45°、右转 45°等变化时，分别生成一张保持同一三分区版式的独立变体，只改变指定的表情或脸部朝向，不改变角色身份、服装、身体区和整体构图。

只要角色是写实真人（用户明确要求写实 / 真人 / 照片质感，或参考图是真人照片），还必须读取 `references/controls/realism-quality/anti-ai-realism.md`，把皮肤五变量写入资产 Prompt。不要只写「真实皮肤」，也不要把三分区角色板误判成原图保真增强。动漫、插画、像素等 stylized 角色不加载这页。

### 6. 场景资产 `scene-assets`

生成场景总览、空景、站位图、道具关系、空间动线和镜头入口等资产。

### 7. 分镜资产 `storyboard-assets`

生成逐镜关键帧、动作拆解、故事板总板和控制型分镜资产。

### 8. 视频参考帧 `video-reference-frames`

生成图生视频使用的首帧、尾帧和关键过渡帧。

不要把角色、场景、分镜和参考帧统称为同一种资产图。

## 第二步：判断图片是否与当前任务相关

先做语义相关性判断，再决定输入 Reference。不要把“消息里带了图片”等同于“当前 Prompt 必须使用图片”。

每张附件先归入一种运行职责：

```text
GENERATION_INPUT
- 最终生图时仍需要把这张图作为模型输入
- 例如身份参考、服装参考、场景参考、姿态参考、待编辑画布

ANALYSIS_SOURCE
- 只用于分析、反推、拆解或提取视觉规律
- 最终 Prompt 可以脱离这张图独立执行

CONTEXT_ONLY
- 只帮助理解当前会话或需求背景
- 不应被绑定进最终生成

IRRELEVANT
- 当前提示词没有使用它，可能是误接、历史附件或无关图片
- 必须忽略，不能污染任务或 Finalizer 路由
```

然后选择输入 Reference：

- 没有图片，或所有附件均为 `IRRELEVANT` → 读取 `references/inputs/text-input-expansion.md`；
- 恰好 1 张与当前任务相关的图片 → 读取 `references/inputs/single-image-reference.md`；
- 2 张及以上与当前任务相关的图片 → 读取 `references/inputs/multi-image-reference.md`。

`ANALYSIS_SOURCE` 和 `CONTEXT_ONLY` 可以参与理解，但不会自动成为最终生成输入；`IRRELEVANT` 完全不进入 Reference Role Map。

多图输入时不要平均融合。必须自动判断每张相关图片的职责，以及人物、服装、场景、构图、光影和风格分别由哪张图提供。

## 第三步：确定 Finalizer Route

**Task Route 与 Finalizer Route 是两套独立判断。**

Finalizer 只回答一个问题：

> 最终用户拿到这份 Prompt 真正执行生图时，是否仍必须提供一张或多张输入图片？

### T2I Finalizer

满足以下条件时走 T2I：

- 最终 Prompt 可以脱离所有当前附件独立生成；
- 当前附件只是 `ANALYSIS_SOURCE`、`CONTEXT_ONLY` 或 `IRRELEVANT`；
- 典型例子：看图反推独立 Prompt、分析海报后产出通用模板、误带图片但当前需求是全新文本生图。

### Edit Finalizer

只要最终生成仍需要至少一张 `GENERATION_INPUT`，就走 Edit：

- 在原图上局部或整体修改；
- 用人物参考保持身份生成新的写真、角色板、海报或新场景；
- 多图换装、合成、换背景、身份/姿态/服装绑定；
- 任意 reference-conditioned generation，只要最终执行仍依赖参考图。

### 路由示例

| 用户需求 | 图片职责 | Finalizer |
|---|---|---|
| “分析这张照片，反推一个以后可独立生成的 Prompt” | ANALYSIS_SOURCE | T2I |
| “分析这张海报，给我通用版式 Prompt 模板” | ANALYSIS_SOURCE | T2I |
| “按这张人物照做三分区角色图，五官保持一致” | GENERATION_INPUT / identity | Edit |
| “图1人物穿图2衣服” | GENERATION_INPUT / identity + outfit | Edit |
| 上传图片但提示词只要求全新的赛博朋克城市 | IRRELEVANT | T2I |
| “保持原图人物，只换背景” | GENERATION_INPUT / canvas + identity | Edit |

## 第四步：判断模式

### 快速模式

除非用户明确要求交互共创，否则默认使用快速模式。

快速模式是全自动执行模式：

- 不向用户追问；
- 不要求用户确认；
- 不提供 A / B / C 选择题；
- 不展示分析、推理、自动补全项、Image Role Map、Finalizer Route 或方向决策；
- 信息不足时自行使用当前请求、会话上下文、相关参考图、任务 Playbook 和最小风险默认值完成补全；
- 信息冲突时自行裁决，只保留最符合核心目标的一条路线；
- 多图冲突时自动分配主参考与辅助参考职责；
- 不因为缺少非必要细节而中断输出。

快速模式读取：

- 当前输入 Reference；
- 当前任务 Playbook；
- 按需 controls、libraries 和 style；
- `assets/templates/prompt-finalization-contract.md`；
- `assets/templates/mode-quick-output-contract.md`。

快速模式不读取结构化任务交付模板，除非用户明确要求完整文档式输出。

#### 自动补全优先级

```text
用户当前明确要求
→ 必须保留或必须修改内容
→ 当前会话上下文
→ 与当前任务相关的参考图可见信息
→ 当前任务 Playbook
→ 已加载 controls / libraries / style
→ 最小风险默认值
```

#### 冲突裁决

- 主目标优先于次要修饰；
- 明确保留项优先于风格改写；
- 局部编辑优先保持未指定区域不变；
- 多图未指定职责时，根据用户语义确定 canvas / identity / outfit / pose / scene 等职责，不固定“第一张图负责全部”；
- 互斥目标只选择最符合核心任务的一项，不输出多个方案；
- 缺少角色信息时补充稳定、可延续、不过度设定的身份锚点；
- 缺少场景信息时只补足可视化所需的最少空间、光线和道具。

### 交互模式

只有用户明确要求共同讨论、脑暴、逐步设计、先提问、比较方向或暂不直接生成时才进入。

规则：

- 每次只问一个问题；
- 只问当前最影响结果的变量；
- 每个问题给出推荐答案；
- 已确认的信息不重复询问；
- 能推断则不追问；
- 允许指出模糊、冲突或不可同时满足的要求；
- 用户喊停、要求直接出结果，或剩余问题只影响轻微细节时立即收口。

交互模式读取：

- 当前输入 Reference；
- 当前任务 Playbook；
- 按需 controls、libraries 和 style；
- `assets/templates/prompt-finalization-contract.md`；
- `assets/templates/mode-interactive-output-contract.md`；
- 最终需要完整结构化交付时，再读取当前任务模板。

### 交互追问优先级

- 成片生图：创作意图 → 主体气质 → 观看距离 → 光影情绪 → 风格强化
- 整体图生图：保留锚点 → 改写强度 → 新画面目标 → 允许变化 → 禁止继承
- 局部图片编辑：编辑目标 → 必须保留 → 目标位置与数量 → 禁止变化 → 文字准确性。若目标是保真细节增强，优先确认皮肤责任区和纹理强度，不要问场景或构图。
- Prompt 反推：复现 / 结构 / 改造路线 → 最终 Prompt 是否依赖原图 → 主要视觉机制 → 可替换槽位 → 禁止继承
- 角色资产：固定身份 → 固定外貌 → 发型服装配色 → 资产包结构 → 可变项。写实真人时皮肤按 anti-ai-realism 默认补全，不追问毛孔写法。
- 场景资产：空间用途 → 出入口与动线 → 主道具 → 镜头入口 → 光影色调
- 分镜资产：单镜任务 → 镜号顺序 → 动作阶段 → 镜间承接 → 跨镜稳定项
- 视频参考帧：帧类型 → 跨帧固定项 → 可运动项 → 起止关系 → 禁止突变

## Reference 读取流程

1. 读取 `references/index.md`。
2. 先做任务语义和图片相关性判断。
3. 固定读取：
   - `1` 份 input Reference；
   - `1` 份 task Reference。
4. 按需读取：
   - `0-2` 份 controls；
   - `0-2` 份 libraries；
   - `0-1` 份 style；
   - `0-1` 份 diagnostic。
5. 根据相关图片职责确定 Finalizer Route，不按附件数量直接判断 T2I / Edit。
6. 在最终输出前固定读取 `assets/templates/prompt-finalization-contract.md`，执行 Prompt Finalization、Final Output Gate、QC、自动修复和 QC 复检。
7. 根据模式读取一份 mode output contract。
8. 分类索引、Prompt Finalization Contract 和 mode output contract 不计入业务 Reference 数量。
9. 不为了凑满额度而读取资料；同一文件被多个入口命中时只读取一次。
10. 只有用户反馈效果不好、参考冲突或问题跨多个维度时才读取 diagnostics。

## Reference 职责

- `inputs/`：如何理解文字、单图和多图输入
- `tasks/`：任务目标、执行流程和视觉交付内容
- `controls/`：如何判断、选择、协调和控制
- `libraries/`：具体选择器、详细资料和知识库
- `styles/`：某种视觉风格如何实现
- `diagnostics/`：跨任务、跨维度综合诊断
- `assets/templates/prompt-finalization-contract.md`：把完整视觉意图编译成 canonical Prompt，并负责最终表达、QC 与自动修复
- `assets/templates/mode-*`：最终展示方式；优先级高于任务 Playbook 中的任何历史输出骨架
- `assets/templates/*-template.md`：交互模式或用户明确要求的结构化交付版式

## 信息优先级

发生冲突时按以下顺序处理：

1. 用户当前明确要求
2. 用户明确指定必须保留或必须修改的内容
3. 当前任务 Playbook
4. 当前输入 Reference
5. 已加载的控制规则
6. 已加载的资料库与风格资料
7. 自动补全项

局部编辑任务中，“其他内容保持不变”属于高优先级约束。

Prompt Finalization、QC 和自动修复不得改变以上优先级，只能修正表达、冲突和格式。

## Prompt 组装原则

- 先确定主体与任务目标，再写风格。
- 先写空间、动作和观看关系，再写装饰细节。
- 静态图片写实任务优先按“主体身份与结构 → 场景与事件 → 拍摄者关系与镜头 → 光线 → 材质 → 受控不完美 → 风格 → 相关限制”组织；具体任务 Playbook 已有更细顺序时沿用其顺序。
- 镜头、光影、色彩、材质和情绪必须互相支持。
- 负向限制只针对当前最危险的失败模式，不做无差别堆叠；最终化阶段优先转换为正向视觉状态。
- 参考图任务必须明确：保留什么、修改什么、允许什么变化、禁止什么出现。
- 内部视觉规划与 Reference 组装默认可使用中文；最终 Prompt 的语言、语法和表面格式由 Finalizer Route 和 `assets/templates/prompt-finalization-contract.md` 决定。
- 任务 Playbook 中的画布像素、比例、字段标题或历史输出骨架只属于规划信息；不得直接复制进最终 Prompt，除非 Finalization Contract 明确允许。

## Final Output Gate（硬门禁）

在任何 Prompt 对外输出前，必须按以下顺序完成。**这是运行主链的一部分，不得只依赖外部 Reference 的提醒。**

1. **Task Intent 已确定**：当前任务不是由附件数量推断出来的。
2. **Image Role 已确定**：每张附件属于 `GENERATION_INPUT / ANALYSIS_SOURCE / CONTEXT_ONLY / IRRELEVANT` 之一；无关图片不进入最终 Prompt。
3. **Finalizer Route 已确定**：最终执行仍依赖图片 → Edit；否则 → T2I。
4. **User Lock 全部存活**：主体、数量、颜色、位置、动作、文字、保留项和明确比例不得被“优化”覆盖。
5. **T2I Grammar**：英文、现在时、第三人称、observer prose、单一连续正文；不使用 `create / generate / make sure / the AI should` 等命令式渲染器语言。
6. **Edit Grammar**：先写编辑操作，只详细描述被修改属性；未指定内容使用高层 preservation；身份来自参考图时优先绑定来源图，不用文字重新雕刻五官。
7. **Image Binding**：Edit 中只引用 `GENERATION_INPUT`。单张生成输入自然称呼图片；两张及以上生成输入在支持标签的目标环境中使用 `<image1> / <image2> ...`，并明确各自职责。`ANALYSIS_SOURCE` 不得混入这些标签。
8. **Text Literalness**：真正需要渲染的可读文字逐字放在直双引号内；不自造用户未提供且无法确认的文案。
9. **Prompt Hygiene**：禁止 tag soup、重复句、互斥描述、无关叙事和 `masterpiece / 8K / award-winning / highly detailed` 等空泛 booster。
10. **Parameter Separation**：数字画幅、像素和 API 参数不写入 canonical prompt 正文；普通纯 Prompt 模式只保留 `vertical / wide / square / crop / framing` 等可见构图语义。Qwen 结构化模式再由字段承载 `wh_ratio / ratio_follow`。
11. **QC 必须有结果**：内部将 Hard Checks 判定为 `PASS` 或 `FAIL`；`FAIL` 不允许直接输出。
12. **Auto Repair 后复检**：失败时只做最小修补，再完整跑一次 Hard Checks；最终只能输出复检 `PASS` 的版本。

若当前 Agent 具备终端/脚本执行能力，并且可以访问本 Skill 仓库，最终候选 Prompt 应优先调用 `scripts/validate_final_prompt.py` 做结构级校验；脚本只负责可机械判断的规则，语义级身份、空间和用户锁仍必须由上述 Gate 检查。没有终端能力时，仍必须按同一 Gate 内部执行，不得跳过。

## 输出前 QC

Final Output Gate 是硬门禁；下面的检查补充语义质量：

- 主体是否唯一清楚；
- 场景是否可视觉化；
- 动作、重心和接触关系是否成立；
- 镜头与光影是否互相支持；
- 参考图职责是否清楚且没有跨属性污染；
- 固定项与可变项是否混淆；
- 限制项是否与任务直接相关；
- 是否出现互相冲突的要求；
- 图片内可读文字是否逐字准确；
- 当前输出是否符合快速或交互模式合同。

任一 Hard Check 失败时不得直接输出，必须先按 `assets/templates/prompt-finalization-contract.md` 自动修复并复检。

## 输出要求

### 快速模式

单 Prompt 任务只输出最终 Prompt 正文：

- 不显示标题；
- 不显示“最终 Prompt”字样；
- 不显示画面概述；
- 不单列限制项；
- 不显示自动补全项；
- 不显示 Image Role / Finalizer Route；
- 不显示方向决策；
- 不显示 QC 或自动修复过程；
- 不附加使用说明或结尾追问；
- 可以使用一个代码块承载 Prompt，但代码块前后不附加说明。

资产类任务需要多个独立 Prompt 时，只输出必要的 Prompt Pack 内容。可以用极简编号或分隔符区分，但不添加说明性标题。

用户明确要求 API / JSON / Pipeline / 结构化格式时，以 `assets/templates/prompt-finalization-contract.md` 中对应目标模型的结构化输出规则覆盖普通纯 Prompt 展示方式。

### 交互模式

交互阶段每次只输出当前问题、推荐答案和必要差异。

最终收口时可以按任务需要输出：

- 方向决策摘要；
- 最终 Prompt；
- 有明确价值的备选 Prompt；
- 保留项、修改项和禁止变化项；
- 固定项与可变项；
- 推荐资产结构或执行顺序。

所有最终 Prompt 都必须先通过 Finalization、Final Output Gate、QC、自动修复和 QC 复检。

用户要求完整结构化交付时，读取当前任务对应的 `assets/templates/` 模板。

## 严禁事项

- 快速模式向用户追问或要求确认
- 快速模式输出分析、标题、摘要或补全说明
- 快速模式默认提供多个方向让用户选择
- 仅凭“有图片附件”就强制走 Edit
- 把 `ANALYSIS_SOURCE / CONTEXT_ONLY / IRRELEVANT` 写进最终生成引用
- 不把维护说明写进对外输出
- 不在未必要时解释内部推理
- 不一次性加载整个 Reference 目录
- 不复制同一知识形成多个正文版本
- 不先堆风格词再补主体
- 不用空泛质量词替代可执行视觉变量
- 不跳过 Final Output Gate、QC 与自动修复
- 不让模型表面格式反向修改已确定的主体、身份、构图或参考关系
