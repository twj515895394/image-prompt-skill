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

## 4. 关键边界回归

### image-to-image 与 image-editing

- 整体场景、构图和风格允许重写：`image-to-image`；
- 只改某个对象、文字、动作或区域：`image-editing`；
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
- 只有一个 style 作为当前主要实现方式。

结论：通过。

## 7. 最终结论

```text
回归用例：28
通过：28
阻塞：0
结构性失败：0
```

当前 Reference 架构在仓库级人工路由审计中满足任务唯一命中、正交知识组合、相邻能力隔离和默认加载预算要求。