# Prompt Finalization Contract

## 用途

本合同位于视觉意图组装之后、最终对外输出之前。它不决定“画什么”，只负责把已经确定的主体、场景、动作、镜头、光影、材质、风格、参考关系和限制，编译成稳定、可执行、跨模型可迁移的最终 Prompt。

canonical grammar 以 Qwen-Image-2.1 Prompt Rewriting / Edit Prompt Enhancer 的核心规则为基线。GPT Image、Nano Banana 等模型可以复用同一语义骨架，但只允许修改表面输入格式、图片引用语法或必要长度限制；不得借“跨模型适配”放宽 T2I / Edit 的硬规则。

本合同属于运行输出层，不计入 `controls / libraries / styles / diagnostics` 的业务 Reference 加载预算。

## 执行顺序

每次准备交付最终 Prompt 或 Prompt Pack 时都必须执行：

```text
Task Intent
→ Image Relevance / Role
→ Finalizer Route
→ Visual Intent
→ Canonical Prompt Finalization
→ Final Output Gate
→ QC
→ Auto Repair
→ QC Re-check
→ Mode Output Contract
→ User Output
```

交互模式只在最终收口时执行；中间讨论不执行最终化。

## 1. Finalizer Route：不按附件数量判断

先给每张当前附件分配运行职责：

```text
GENERATION_INPUT
- 最终真正生图时仍要作为模型输入
- 例如 canvas、identity、outfit、pose、scene、style reference

ANALYSIS_SOURCE
- 只用于反推、分析、拆解、提取构图/光影/风格规律
- 最终 Prompt 可以脱离该图执行

CONTEXT_ONLY
- 只帮助理解需求背景
- 不参与最终生成

IRRELEVANT
- 当前提示词没有使用该图
- 误接、历史附件或无关图片
- 完全忽略
```

然后判断：

```text
最终执行 Prompt 时需要 >= 1 个 GENERATION_INPUT
→ Edit Finalizer

最终执行 Prompt 时不需要任何 GENERATION_INPUT
→ T2I Finalizer
```

### 必须遵守的例子

- 看图反推一个以后可独立生成的 Prompt → 图片是 `ANALYSIS_SOURCE` → T2I；
- 看图分析版式并给通用模板 → `ANALYSIS_SOURCE` → T2I；
- 根据人物参考图重新做写真 / 海报 / 三分区角色图，并要求保持身份 → `GENERATION_INPUT / identity` → Edit；
- 图 1 人物换图 2 衣服 → 两张都是 `GENERATION_INPUT` → Edit；
- 消息带图但用户当前只要求一个无关的全新文本场景 → 图片 `IRRELEVANT` → T2I；
- 只修改原图局部 → 原图 `GENERATION_INPUT / canvas` → Edit。

**Task Route 与 Finalizer Route 必须分开。** `prompt-reverse-engineering` 可以最终走 T2I，也可以最终走 Edit；`character-assets` 也可以因为是否继续依赖身份参考图而走不同 Finalizer。

## 2. 先锁定用户固定项

Finalization、QC 和自动修复都不能擅自改变：

- 主体、对象与数量；
- 明确颜色；
- 前后左右、上下、遮挡、层级等空间关系；
- 动作、姿态、表情和视线；
- 服装、道具、材质；
- 景别、机位、构图和明确裁切；
- 时间、天气、场景；
- 必须保留 / 必须修改的参考属性；
- 图片内可读文字及其标点、大小写、语言和顺序；
- 用户明确给出的用途和比例意图。

自动补全只能填空，不能借“优化”覆盖固定项。

## 3. T2I Canonical Grammar

只有当最终 Prompt 可以脱离当前图片独立执行时使用。

### 3.1 语言与叙述视角

- 默认使用英文描述性 prose；
- 现在时、第三人称、observer perspective；
- 描述“最终画面已经是什么样”，而不是给模型下命令；
- 不使用 `create`、`generate`、`make sure`、`please`、`the AI should` 等渲染器指令；
- 不使用 tag soup；
- 不用 `masterpiece`、`8K`、`award-winning`、`highly detailed` 等空泛 booster 代替可观察视觉信息。

### 3.2 开头建立整张图

第一句优先包含：

```text
orientation / framing
+ medium / style
+ main subject
+ background / palette
```

Medium 不省略，例如 photograph、portrait、poster、illustration、character sheet、infographic、3D render。

### 3.3 按画面关系展开

复杂多区域画面优先按区域组织：

```text
background / surface
→ top
→ left
→ center
→ right
→ bottom / foreground
```

单主体优先按：

```text
background / depth
→ subject placement / posture
→ face / head
→ body / garments / surface
→ contact objects
→ remaining environment
```

复杂画面通常需要足够的位置锚点；简单单主体不机械凑数量。

### 3.4 人物与材质

只写可观察信息：build、posture、gaze、expression、hair、visible skin characteristics、garment construction、folds、contact relationship。

颜色和材质具体化，例如 muted olive、off-white、ribbed cotton、weathered concrete、brushed metal、frosted glass；用户已给出的颜色不得自行替换。

### 3.5 图片中文字

所有真正需要读出来的文字使用直双引号，保持用户指定的原语言、标点、大小写和顺序。

无法确认的背景小字不要臆造，可以描述为 blurred、indistinct、too small to read。

### 3.6 光线与物理关系

明确与稳定生成相关的：

```text
light source
+ direction
+ quality
+ shadow / highlight response
```

同时检查阴影、反射、尺度、重力、地面接触、座椅接触、服装和头发运动是否自洽。

### 3.7 结尾

只用一句 whole-frame composition / design / mood summary 收束，不连续堆叠同义总结。

### 3.8 长度

Qwen 官方典型完整场景可接近约 20 句、400–500 英文词，但本 Skill 不机械凑字数：

- 简单主体：只补真正影响生成稳定性的细节；
- 常规完整场景：充分描述空间、材质、光线和构图；
- 海报、多人、多区域、信息密集画面：允许接近官方长描述密度。

无论长短，都不能退化成关键词列表，也不能为凑长度发明无关道具、文字或背景故事。

## 4. Edit Canonical Grammar

只要最终生成仍依赖任何 `GENERATION_INPUT` 就使用。

Edit 不等于“只能局部修图”。只要人物、产品、服装、场景等来自输入图片，即使最终要重新设计一个全新的写真、角色板、海报或新场景，仍属于 reference-conditioned Edit。

### 4.1 语言

描述性指令语言：

- 中文用户指令 → 中文；
- 英文用户指令 → 英文；
- 其他语言 → 默认英文，除非用户明确要求目标语言。

图片内实际渲染文字仍按用户指定文字 / 输入图主导文字语言 / 当前需求决定，不与描述性 prose 混淆。

### 4.2 属性解耦

只详细描述需要改变的属性，并让变化足够明确；未被点名的内容保持输入 fidelity。

同时防止：

- **Leakage**：换衣服时顺便重绘脸、发型、构图、背景；
- **Under-editing**：变化过弱，几乎看不出请求被执行。

### 4.3 Preservation 不要重画

未修改内容优先用一条高层 preservation clause 概括，例如：

```text
保持人物身份、未指定外观、姿态、构图、背景及其他未编辑内容与输入一致。
```

不要为了“锁定”而重新逐项详细描述原脸或原背景；那会把 preservation 变成新的重绘指令。

### 4.4 身份优先绑定来源图

身份来自参考图时，优先指向图片来源，不用文字重新雕刻眼睛、鼻子、嘴唇等五官。

只有 `GENERATION_INPUT` 才进入最终 Reference Role Map。

多图例子：

```text
<image1> canvas + identity
<image2> outfit only
<image3> pose only
<image4> scene only
```

每张图只提供被分配属性，辅助图不得把人脸、身材、背景或风格跨职责污染到其他对象。

### 4.5 图片标签

- 最终只有 1 张 `GENERATION_INPUT`：正文自然称“图像 / 图片中 / the image”，不写 `<image1>`；
- 最终有 2 张及以上 `GENERATION_INPUT`：在支持显式标签的目标环境中使用 `<image1>`、`<image2>`…，并逐张说明职责；
- `ANALYSIS_SOURCE / CONTEXT_ONLY / IRRELEVANT` 永远不进入这些标签编号；
- 其他模型不支持 Qwen 标签时只替换引用语法，不改变 Role Map。

### 4.6 新暴露区域

删除、移动、扩图或替换物体后，只补充必要的墙面、地面、纹理、光照、透视和遮挡连续性；不要顺手清理用户未要求处理的缺陷或杂物。

### 4.7 负向限制

优先改写为正向可观察状态，例如：

```text
不要自拍、不要出现手机
```

优先变为：

```text
由画面外第二人拍摄，摄影者与手机始终位于可见画面之外。
```

只有无法可靠正向化、且属于当前高风险失败模式时，才保留最短必要排除。

## 5. 参数与 Prompt 正文分离

### 通用

数字画幅、像素和 API 参数属于生成参数，不属于 canonical prompt 的视觉正文。

Prompt 正文可以保留：

- vertical / horizontal / square / wide / tall；
- framing / crop / subject occupancy；
- 版式区域比例（例如 22% + 22% + 56%）在它本身就是可见布局设计时可以保留。

Prompt 正文默认不写：

- `16:9 / 9:16 / 3:2` 等数字画幅；
- `1920×1080 / 1080p` 等像素或分辨率；
- `2K / 4K / 8K` 作为质量 booster；
- API 字段名。

任务 Playbook 中出现的像素、画幅和历史模板字段属于规划信息，Finalizer 必须重新分类后再决定是否进入正文，不能直接复制。

### Qwen 结构化输出

当用户明确要求 Qwen API、JSON、Pipeline 或结构化格式时：

- T2I：`rewritten_prompt` + `wh_ratio`；
- Edit：`rewritten_prompt` + `wh_ratio` + `ratio_follow`；
- `wh_ratio` 与 `ratio_follow` 互斥；
- 比例、像素不写进 `rewritten_prompt`；
- Edit 的 `ratio_follow` 指向真正 canvas generation input。

### 其他模型

GPT Image、Nano Banana 或其他模型只能替换必要的参数字段、图片引用语法或输入包装方式；canonical prompt 的 T2I / Edit 规则不因模型变化而被放宽。

## 6. Final Output Gate

在对外输出前，内部必须得到一个明确 Gate 结果：

```text
ROUTE = T2I | EDIT
GENERATION_INPUT_COUNT = N
USER_LOCK = PASS | FAIL
TASK_GRAMMAR = PASS | FAIL
REFERENCE_BINDING = PASS | FAIL
IDENTITY = PASS | FAIL
SPATIAL_COHERENCE = PASS | FAIL
PHYSICAL_COHERENCE = PASS | FAIL
TEXT_LITERALNESS = PASS | FAIL
PROMPT_HYGIENE = PASS | FAIL
PARAMETER_SEPARATION = PASS | FAIL
FORMAT = PASS | FAIL
FINAL_GATE = PASS | FAIL
```

这些字段只用于内部检查，不对用户展示。

只要任一 Hard Check 为 FAIL，`FINAL_GATE` 就必须是 FAIL，禁止直接输出候选 Prompt。

### Hard Checks

1. **Route**：Finalizer Route 是否由最终图片依赖决定，而不是附件数量；
2. **User Lock**：用户固定项是否全部存活；
3. **Task Grammar**：T2I / Edit 语法是否正确；
4. **Reference Binding**：是否只引用 generation inputs，且职责唯一；
5. **Identity**：要求保持身份时是否发生重绘或参考污染；
6. **Spatial Coherence**：位置、遮挡、裁切、主体占比是否兼容；
7. **Physical Coherence**：光源、阴影、反射、重力、接触和尺度是否成立；
8. **Text Literalness**：所有可读文字是否逐字准确，没有自造额外文案；
9. **Prompt Hygiene**：无 tag soup、重复、互斥、无关叙事和空泛 booster；
10. **Parameter Separation**：数字比例、像素和 API 参数是否泄漏进正文；
11. **Format**：是否符合当前 mode output contract / 目标模型结构化合同。

### Soft Checks

- 信息顺序是否自然；
- 细节密度是否符合景别；
- 简单画面是否被过度扩写；
- 复杂画面是否缺少关键空间锚点；
- 风格词是否已经转成可观察视觉属性；
- 真实感是否错误依赖“颗粒 / 瑕疵 / 8K”等词。

## 7. 自动修复

`FINAL_GATE = FAIL` 时自动修复，不把失败草稿交给用户。

顺序：

```text
1. 恢复 User Lock
2. 修正 Finalizer Route / T2I-Edit Grammar
3. 修正 Generation Input Role / Identity Pollution
4. 消除互斥空间、动作、镜头和光线
5. 恢复图片内文字逐字准确性
6. 删除重复、tag soup、booster 和无关扩写
7. 把可转换的负向限制改成正向视觉状态
8. 补真正缺失的空间、材质或光照信息
9. 修正参数分离和目标模型表面格式
```

采用最小补丁，不重新设计整份 Prompt。

修复后完整重跑 Hard Checks；最多两轮。两轮后仍冲突时按以下优先级裁决：

```text
用户当前明确要求
→ 明确保留 / 必须修改项
→ 身份与参考绑定
→ 当前任务 Playbook
→ 输入 Reference
→ 已加载 controls / libraries / styles
→ 自动补全项
```

最终只能输出 `FINAL_GATE = PASS` 的版本。

## 8. 可执行 Validator

如果当前 Agent 具备终端执行能力，并且可以访问 Skill 仓库，候选 Prompt 应优先调用：

```bash
python scripts/validate_final_prompt.py --mode t2i --prompt "..."
python scripts/validate_final_prompt.py --mode edit --generation-input-count 2 --prompt "..."
```

结构化 Qwen JSON 可使用 `--json-file` 校验。

Validator 只检查能机械判断的结构规则：booster、命令式 T2I、图片标签数量、比例/像素泄漏、结构化字段互斥等。身份、空间、User Lock、编辑泄漏等语义规则仍由 Final Output Gate 判断。

没有终端能力时不得跳过 QC，只是改为按同一 Gate 内部执行。

## 最终原则

最终 Prompt 必须同时满足：

```text
内容由 Task / Input / Reference 决定
+ Finalizer Route 由最终图片依赖决定
+ T2I 使用 canonical observer prose
+ Edit 使用强属性解耦与 reference binding
+ 模型 adapter 不放宽 canonical hard rules
+ Final Output Gate 必须 PASS
+ FAIL 自动最小修复并复检
```

不要让模型规范层反向覆盖已经确定的视觉设计，也不要让无关附件改变最终 Prompt 语法。
