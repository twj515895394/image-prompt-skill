# 用户整理资料摄取映射（2026-07-10）

## 状态说明

| 状态 | 含义 |
|---|---|
| `merge-existing` | 与现有正式叶子高度重合，优先补充现有文件 |
| `split-and-merge` | 同时包含多层职责，需要拆分后分别合并 |
| `candidate-new-leaf` | 当前架构存在明确缺口，可提炼为新叶子 |
| `migration-source-only` | 适合作为迁移资料，不应原样成为运行时叶子 |
| `pending-audit` | 仍需与正式文件逐段查重 |

## 初步映射

| 原始资料 | 初步状态 | 预定正式归属 | 处理说明 |
|---|---|---|---|
| 人物外貌与写真Prompt结构.md | `split-and-merge` | `libraries/human/`、`controls/prompt-assembly/`、摄影风格叶子 | 拆分人物外貌选项、写真组装规则和联动关系，不建立同名万能页 |
| 女友感场景写真Prompt框架.md | `merge-existing` / `candidate-new-leaf` | `styles/photography/lifestyle-candid-photography.md` 或细分 lifestyle portrait 叶子 | 先补现有生活化纪实摄影；仅在路由条件足够独立时新建叶子 |
| 女主妆容选择器.md | `merge-existing` | `references/libraries/human/female-makeup-selector.md` | 与现有叶子高度重合，仅补缺失分类、联动和限制 |
| 角色资产生成结构.md | `merge-existing` | `references/tasks/character-assets/playbook.md`、identity controls | 补固定锚点、生成顺序和细节资产清单，不另建任务页 |
| 场景资产与空间规划.md | `split-and-merge` | `references/tasks/scene-assets/playbook.md`、`controls/spatial-blocking/` | 任务流程进入 Playbook；站位公式和空间控制进入 controls |
| 分镜资产与image2故事版.md | `merge-existing` | `references/tasks/storyboard-assets/playbook.md`、composition libraries | 7 类故事板作为任务内部选择，不新增一级任务 |
| 角色发型选择器.md | `merge-existing` | `references/libraries/human/hairstyle-selector.md` | 补长度、形态、实验风和动态规则 |
| 表情与微表情选择器.md | `split-and-merge` | `libraries/human/expression-selector.md`、`controls/pose-action/lifestyle-micro-expression.md` | 表情选项与自然发生机制分开维护 |
| 视角机位与景别选择器.md | `candidate-new-leaf` | `controls/composition-camera/shot-angle-lens-selection.md` | 当前通用景别、机位、焦段和透视叶子缺失 |
| 电影光影与色调选择器.md | `split-and-merge` | `controls/lighting-color/cinematic-lighting-patterns.md`、`libraries/lighting-color/cinematic-color-palettes.md` | 光影判断方法与色调选项分开维护 |
| 生图风格选择器.md | `migration-source-only` | 各 `references/styles/*` 分类 | 范围过大，不原样建立万能选择器；按媒介和实现方法拆分 |
| 影视风格选择器.md | `split-and-merge` | `styles/cinematic/`、必要的 camera/light controls | 题材级影视视觉进入 cinematic；设备和镜头执行不混入风格页 |
| 基础Prompt结构.md | `merge-existing` | `controls/prompt-assembly/`、各任务 Playbook | 作为通用组装规则补充，避免形成第二套最终输出结构 |
| 电影感Prompt拆解公式.md | `candidate-new-leaf` | `styles/cinematic/film-still-language.md` | 提炼“电影画面如何实现”，镜头和光影细节继续下钻 controls |
| 图像风格提取流程.md | `merge-existing` | `inputs/single-image-reference.md`、`tasks/prompt-reverse-engineering/playbook.md` | 输入识别与反推任务职责分开补充 |

## 建议首批正式处理顺序

1. 通用镜头：`视角机位与景别选择器.md`
2. 电影光影与色调：拆为控制叶子和资料选择器
3. 电影画面语言：合并 `电影感Prompt拆解公式.md` 与 `影视风格选择器.md` 的稳定共性
4. 现有人物选择器增补：妆容、发型、表情
5. 任务 Playbook 增补：角色、场景、分镜
6. 人物写真、女友感与综合生图风格资料的后续拆分

## 每批迁移验证要求

每批正式写入至少验证：

1. 正常任务能够命中新叶子或更新后的叶子；
2. 相邻任务不会误加载；
3. 与现有 Reference 联动时不重复加载同一知识；
4. 索引只保留读取条件和目标路径；
5. 正式叶子不引用本临时目录作为运行时依赖。
