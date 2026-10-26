# Image Prompt Skill 最终行为路由回归

## 1. 验证定位

本回归用于验证当前 Reference 架构能否把典型请求路由到最小且正确的知识组合。

它验证的是：

- 输入类型判断；
- 任务 Playbook 唯一命中；
- controls、libraries、style 和 diagnostic 的按需组合；
- 相邻能力不误加载；
- 默认加载预算；
- 新增外部知识与原有任务体系的兼容性。

它不是图像模型端到端画质评测。模型输出仍需要在真实生成环境中观察。

## 2. 默认预算

```text
固定：
1 input
1 task

按需：
0–2 controls
0–2 libraries
0–1 style
0–1 diagnostic
```

分类索引不计入业务 Reference 数量。

## 3. 回归用例

| # | 用户请求摘要 | 预期任务 | 关键按需 Reference | 不应误加载 | 结果 |
|---:|---|---|---|---|---|
| 1 | 纯文字生成自然办公室人物照片 | finished-image | office environment、office camera、office mixed light、lifestyle candid | product、comic、game asset | 通过 |
| 2 | 单图整体改成雨夜都市风格 | image-to-image | single-image-reference、cinematic light / film still 按目标选择 | image-editing | 通过 |
| 3 | 多图组合人物 A、服装 B、场景 C | image-to-image | multi-image-reference、reference handling | 平均融合、额外人物 | 通过 |
| 4 | 只把桌上水果替换成卫生纸 | image-editing | 局部编辑合同、空间与数量约束 | 整体图生图 | 通过 |
| 5 | 只修改聊天气泡中的准确文字 | image-editing | 文字准确性、必须保留 / 修改 / 禁止变化 | 海报重设计 | 通过 |
| 6 | 从参考图反推可复现 Prompt | prompt-reverse-engineering | single-image-reference、复现型路线 | 改造型默认扩写 | 通过 |
| 7 | 提炼参考图的可替换风格公式 | prompt-reverse-engineering | 结构型路线、风格机制拆解 | 复制原图具体身份 | 通过 |
| 8 | 角色三视图、头像和表情资产 | character-assets | character identity、human selectors | scene-assets、finished comic | 通过 |
| 9 | 游戏角色 Sprite Sheet | character-assets | game asset presentation、pixel art、identity control | cinematic anime key visual | 通过 |
| 10 | 办公室场景总览、空景和动线图 | scene-assets | scene playbook、spatial blocking、environment library | 人物写真 style | 通过 |
| 11 | 等距模拟经营基地和功能分区 | scene-assets | game asset presentation、isometric miniature world、spatial control | product visualization | 通过 |
| 12 | 8 镜控制型视频故事板 | storyboard-assets | storyboard board types、spatial blocking、identity | comic visual language 默认加载 | 通过 |
| 13 | 6 格黑白动作漫画成品页 | finished-image | comic panel layouts、multi-panel continuity、sequential comic style | 技术型故事板镜号与时间轴 | 通过 |
| 14 | 视频首帧、尾帧和过渡关键帧 | video-reference-frames | frame state、identity / spatial 按需 | 完整视频时序 Prompt | 通过 |
| 15 | 白底陶瓷杯电商主图 | finished-image | product display、hero composition、studio lighting、product photography | 3D exploded view | 通过 |
| 16 | 耳机内部结构爆炸图 | finished-image | product display、product visualization、hero composition | 真实产品摄影作为唯一 style | 通过 |
| 17 | 竖版人物活动海报 | finished-image | poster layout、text-image hierarchy | infographic 默认加载 | 通过 |
| 18 | 五步部署流程信息图 | finished-image | infographic visual language、text hierarchy 按需 | 虚构精确数据 | 通过 |
| 19 | 雨夜分手后的电影剧照 | finished-image | film still、cinematic lighting / palette | lifestyle candid | 通过 |
| 20 | 旅行杂志环境人像 | finished-image | environmental editorial portrait、camera / light 按需 | film still 剧情事件 | 通过 |
| 21 | 伴侣同行时随手拍到的生活照 | finished-image | lifestyle candid、micro-expression、candid composition | environmental editorial pose | 通过 |
| 22 | 动画电影级游戏角色主视觉 | finished-image | cinematic anime key visual、camera / light 按需 | character asset board | 通过 |
| 23 | 统一像素尺度的战斗场景 | finished-image | pixel-art visual language、game asset presentation 按需 | ordinary anime rendering | 通过 |
| 24 | 多图参考互相冲突且效果失败 | 当前任务 + diagnostic | reference-conflict diagnostic | 默认读取全部 diagnostics | 通过 |
| 25 | 普通无文字电影剧照 | finished-image | film still | typography、infographic | 通过 |
| 26 | 单幅韩漫人物插画 | finished-image | comic / manhwa style | comic panels、multi-panel continuity | 通过 |
| 27 | 普通真人办公室照片 | finished-image | photography route | pixel art、isometric、anime key visual | 通过 |
| 28 | 产品与人物混合品牌广告 | finished-image | 单一主 style，product controls 与 portrait / layout 按目标组合 | 同时加载多个互斥 style | 通过 |
| 29 | 已有人像只补皮肤纹理、不重新设计 | image-editing | fidelity-detail-enhancement | anti-ai-realism、image-to-image | 通过 |
| 30 | 从文字生成看不出 AI 的生活抓拍 | finished-image | anti-ai-realism | fidelity-detail-enhancement | 通过 |
| 31 | 窗边中近景人像，皮肤要真实不要塑料 | finished-image | anti-ai-realism 皮肤五变量 | fidelity-detail-enhancement、单独皮肤库 | 通过 |
| 32 | 参考真人照片做竖版角色身份参考板 | character-assets | identity-consistency + anti-ai-realism；9:16 上 1 下 3 四格 | fidelity-detail-enhancement、动漫皮肤颗粒；上方只含正脸头部且不露颈肩，正面身体必须无头，侧脸与正脸身份一致 | 通过 |
| 33 | 普通室内人物照片，要求自然可拍且不过度精修 | finished-image | anti-ai-realism，按需 camera / light | fidelity-detail-enhancement、随机瑕疵堆叠 | 通过 |
| 34 | 白底陶瓷杯电商主图，要求洁净对称 | finished-image | product display、hero composition、studio lighting、product photography | 强制生活纪实瑕疵、随机旧化 | 通过 |
| 35 | 远景人物要求真实但不强调皮肤细节 | finished-image | anti-ai-realism，按景别降低皮肤纹理密度 | 近景五变量全量铺写 | 通过 |
| 36 | 只用噪点、颗粒和全局锐化制造真实感 | finished-image | anti-ai-realism 诊断：回到结构、光线和材质 | 低清废片化、统一皮肤颗粒 | 通过 |
| 37 | 从真人参考图提炼可复用的自然照片 Prompt 结构 | prompt-reverse-engineering | single-image-reference、realism-quality | 无条件复制原人物和原图缺陷 | 通过 |
| 38 | 只给出简短概念，要求直接生成一张有明确视觉重点的成片 | finished-image | text-input-expansion；按画面目标至多加载必要的 controls / style | 因信息少而追问、只扩成通用关键词清单、平均铺满所有维度、添加无关剧情 | 通过 |
| 39 | 东方禅意极简海报，明确允许适当补充并要求留白处配合适文字 | finished-image | text-input-expansion；poster / typography style 按布局需要读取 | 只写古风人物+粉色色块+标题；粉色泛滥；把衣裙当垂落布幔；任意添加文化符号或未授权文案；丢失字面标题；标题、色块和人物平均争夺焦点 | 部分通过：要求基本命中，女性主焦点偏弱 |
| 40 | 给出一张完成度更高的同题材海报作参考，询问分析设计后的 Prompt | prompt-reverse-engineering | single-image-reference；poster layout types；text-image hierarchy | 声称知道参考图原 Prompt；只罗列物件；照搬布局却不解释文字、留白和装饰的关系 | 待真实模型画面复核 |
| 41 | 简短人像、产品、叙事场景或插画需求，未进入交互模式 | 对应唯一任务 Playbook | 对各自关键维度作视觉方案合成 | 把主动设计限制为海报；不同任务都套同一份字段清单；只复述用户名词 | 规则待跨类型生成复核 |
| 42 | 全局古风人物海报中同时出现服装、字体、环境和道具方向 | finished-image | 风格范围判断；按需读取 graphic-design | 古装配现代字形、无历史语境的棚拍背景而未说明为混搭；把单一局部风格词擅自扩展成朝代复原 | 新增风格一致性回归，待真实模型复核 |
| 43 | 任意图片任务包含多个主要元素，并使用“漂亮 / 高级 / 古风 / 精致”等抽象评价 | 对应唯一任务 Playbook；Prompt Finalization | 主元素覆盖度与对象相关的可见特征 | 只精写一个主焦点、把其他主要主体/道具/环境/文字概括带过；用评价词代替形态、状态、材质和关系；把“细致”误做无关微观堆料 | 规则已补，待跨类型生成复核 |
| 44 | 从文字描述生成 9:16 服装设计参考板 | fashion-design | text-input-expansion；按需 material-effect | character-assets 的人脸身份锚点、finished-image 时尚人像构图 | 同一套衣物的正侧背完整视图、3–5 个对应细节、材质样片；模特脸去识别化 | 规则路由审查通过 |
| 45 | 依据服装参考图制作设计板 | fashion-design | single-image-reference；按需 material-effect | 继承参考人物身份、擅改服装结构或添加不存在的装饰 | 参考图绑定服装设计；可见剪裁、颜色、材质与配件忠实一致，未展示部位只作最小补全 | 规则路由审查通过 |
| 46 | 同一角色的身份三视图，要求正脸特写与侧脸一致 | character-assets | identity-consistency + 写实真人时 anti-ai-realism | fashion-design 的去识别化人台与材质样片板 | 保留角色身份参考板的现有默认版式与真人皮肤规则 | 反向路由审查通过 |
| 47 | 单张模特街拍或时尚品牌穿搭主视觉 | finished-image | 按目标读取摄影、光线或产品展示资料 | fashion-design 的技术三视图板 | 以成片人像和场景表达为主，不强制加入正侧背、材料样片与细节格 | 反向路由审查通过 |
| 48 | 在现有人像中更换外套，保持脸、姿态和背景不变 | image-editing | single-image-reference；局部编辑合同 | fashion-design 的整套三视图重构 | 只替换指定服装并保持未指定区域不变 | 反向路由审查通过 |

### Case 43：主要画面元素的通用描述完整度

输入可以是人物海报、产品图、动物肖像、建筑/室内、食物、自然景观、插画或图文封面；用户要求成片且画面中存在多个主要元素。

预期：先为每个主要可见元素写出足以生成的对象相关描述，包括其可辨识形态/组成、状态或用途、画面位置/尺度、与邻近元素的关系，并补充影响目标的材质、色彩或表面细节。把“漂亮”“高级”“精致”“古风”等抽象评价转成该对象适用的可见线索。再按主次给重点元素更多展开，支撑元素少写一层即可；低贡献装饰可以省略。

反向检查：不能因为不是第一焦点，就把关键配角、产品结构、环境锚点、文字图形或支撑道具写成单一名词/抽象标签；也不能把所有物体等量写成微观细节清单，或添加用户未暗示的设定。

### Case 38：简短请求的自主视觉规划

输入：“一张雨夜里等末班车的女孩。”用户未要求讨论，也未指定机位、情绪表达或光线。

预期：保持快速模式；内部确定画面目标和第一视觉落点，从动作瞬间、人物姿态/视线、站台空间、雨夜光线等候选维度中选择最有表现力的少数重点，具体写出重点并简洁补足支撑关系。风格或细节不得改变“等末班车”的题材，不虚构强剧情或关系。最终只输出完整 Prompt，不显示规划过程。

反向检查：不能因为输入简短而只输出“女孩、雨夜、车站、电影感”；也不能无差别写满妆容、背景行人、城市史、多个镜头和无关道具。

### Case 39：开放补充权限与海报设计完整度

输入：用户指定“轻坐有欢”东方禅意极简海报，明确了古风女子、珊瑚粉色块、奶白基底、人物与标题区位置、柔光和 9:16 比例，并要求“画面留白处配上合适的文字”。

预期：所有指定内容保持不变；把“合适的文字”和“适当补充”视为开放但有边界的设计委托。内部为主体、色块、标题和留白建立明确阅读顺序与图形关系，细化色块边界和必要的材质/字体处理，并只补少量能支撑东方禅意极简方向的视觉细节。标题“轻坐有欢”字面准确；如补副文案，须短、相关、明确写出字面内容与层级。垂落布幔要作为独立空间元素描述，不能以人物衣裙替代。不得机械叠加文化符号、引入新故事、破坏奶白/珊瑚粉/柔杏色约束或把留白塞满。

画面评估不设“东方美学”的单一标准；检查用户指定的风格是否由版式、图形、字体、材质和装饰节奏等整体证据承载，而非只由古装与颜色暗示。该用例的 Skill 规则已纳入，模型画面是否达成仍需真实生成复核。

用户附图的具体观察：成图为 1680×2512（约 2:3），没有达到指定的 9:16；标题和人物构成清楚、配色柔和，但珊瑚色块更像摄影棚背景板，古风服装承担了大部分风格提示，版式图形关系和海报层级仍较弱。该观察作为案例诊断，不把它升级成单一东方美学标准。

最新复核图为 1536×2736（接近 9:16），准确呈现标题“轻坐有欢”、副文案、人物坐姿、珊瑚色块和左侧垂落纱幔，配色与柔光也符合要求。构图的不足是大标题、宽阔色块与人物同时占据强势区域；“女性审美爆款型”下人物面部应是主焦点，但缩小观看时面部不够突出。后续应减小标题或色块的视觉权重、适度放大/靠近人物，并让背景退后。此处用“主焦点—次级信息—氛围支撑”描述目标，不将海报固定为主体必然第一。

该 Prompt 还显式要求“现代宋体或人文衬线字体”，而人物是古风造型、背景是现代摄影棚式色块；生成结果忠实呈现了这种现代/古典混合。若用户希望整幅古风，风格范围和跨元素一致性应在 Prompt 阶段明确，不能归咎于图像模型单独失误；若希望当代东方混搭，也应写清设计机制。

对照用户提供的另一张同题材参考图，可观察到更完整的艺术指导：满版珊瑚背景建立稳定承载面；上部书法主标题、副文案、短正文和印章形成明确阅读层级；左侧纱幔建立前景框景并引导视线；右侧竖排短句平衡左侧重量；花枝、发饰和衣料刺绣重复同一花卉母题；人物落在下半部，石质台面承接空间。这里记录的是图中可见的关系，不推断或冒称其原始 Prompt。

## 4. 关键边界回归

### image-to-image 与 image-editing

- 整体场景、构图和风格允许重写：`image-to-image`；
- 只改某个对象、文字、动作或区域：`image-editing`；
- 已有成片只补皮肤微观纹理或有效分辨率：`image-editing` + `fidelity-detail-enhancement`；
- 是否有参考图不是任务边界。

结论：通过。

### 生活抓拍、环境人像与电影剧照

- 生活抓拍：非摆拍、日常事件、关系视角；
- 环境人像：适度引导姿态、人物身份与地点共同表达；
- 电影剧照：剧情事件、关系变化和情绪落点。

结论：通过。

### 漫画页与故事板

- 成品漫画：读者阅读、分格节奏、对白和拟声词；
- 制作故事板：镜号、机位、动作、承接和技术标注。

结论：通过。

### 产品摄影与 3D 可视化

- 真实相机和棚拍逻辑：product photography；
- 爆炸图、剖面、不可能机位和 CGI：product visualization。

结论：通过。

### 游戏资产类型与视觉风格

- 资产交付类型回答输出什么；
- anime、pixel art、isometric 等 style 回答如何呈现；
- 二者可以组合，但不互相替代。

结论：通过。

## 5. 预算回归

所有用例均可保持：

```text
1 input
1 task
最多 2 controls
最多 2 libraries
最多 1 style
最多 1 diagnostic
```

复杂请求需要更多知识时，应拆分交付或只加载决定当前结果的最高价值叶子，不默认突破预算。

## 6. 反例回归

- 无文字成片不加载 typography；
- 单图任务不加载 multi-panel continuity；
- 普通人物写真不加载 product leaves；
- 普通办公室场景不加载 game / pixel / isometric；
- 制作故事板不默认加载成品漫画语言；
- 正常请求不默认读取 diagnostics；
- 只有一个 style 作为当前主要实现方式；
- 已有成片保真增强不加载 anti-ai-realism；
- 从零生成真实照片不加载 fidelity-detail-enhancement；
- 近景真实皮肤不另建皮肤资料库，五变量只存在于 anti-ai-realism；
- 写实角色设计图加载 anti-ai-realism，不加载 fidelity-detail-enhancement；
- 动漫 / 像素角色设计图不加载皮肤五变量。
- 普通自然照片可加载 anti-ai-realism；商业洁净产品图不强制加载生活纪实控制；
- 远景不铺近景级别的皮肤纹理；噪点、颗粒和锐化不替代结构、光线或材质控制。

结论：通过。

## 7. 最终结论

```text
回归用例：43
通过：38 条路由 / 规则审查
已复核：1 条真实模型画面（部分符合，主焦点偏弱）
待复核：1 条真实模型画面
待复核：1 条真实模型画面及 2 条跨类型规则审查
阻塞：0
结构性失败：0
```

当前 Reference 架构在仓库级人工路由审计中满足任务唯一命中、正交知识组合、相邻能力隔离和默认加载预算要求。
