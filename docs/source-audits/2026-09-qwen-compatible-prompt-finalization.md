# 2026-09 Qwen-Compatible Prompt Finalization 来源审计

## 来源

### 1. Qwen-Image-2.1 官方 Prompt Rewrite 规范

- 仓库：`https://github.com/QwenLM/Qwen-Image-2.1`
- T2I 规范：`prompt_rewrite/prompts/system_prompt_t2i.txt`
- Edit 规范：`prompt_rewrite/prompts/system_prompt_edit.txt`
- 访问日期：2026-09-28
- 许可证：Qwen RESEARCH LICENSE AGREEMENT（2026-09-20 版本），仓库材料授权范围包含非商业研究/评估限制；不按开放源码宽松许可证处理。

### 2. iamyoki/qwen-image-2.1-skill

- 仓库：`https://github.com/iamyoki/qwen-image-2.1-skill`
- 关注文件：`SKILL.md`、`references/t2i_rules.md`、`references/edit_rules.md`
- 访问日期：2026-09-28
- 许可证：Apache License 2.0

## 本次使用边界

本次不把 Qwen 官方 system prompt 或第三方 Skill 正文直接复制进正式运行文件，而是只抽象以下可复用机制：

- T2I 使用“观察最终画面”的自然语言描述，而不是命令式 tag soup；
- 空间位置、材质、颜色、光线与物理一致性需要显式表达；
- 图片内可读文字需要按字面锁定；
- Edit 使用 Attribute Disentanglement，只修改目标属性并高层级保持其他内容；
- 多图先明确每张图职责，身份来源优先直接绑定参考图；
- 画幅参数与 Prompt 内容分离；
- 空泛质量 booster 不作为质量控制；
- 输出前执行结构、冲突、身份、文字、空间和格式检查。

这些机制被重新组织为模型无关的 `Prompt Finalization Contract`，使其可作为 Qwen、GPT Image、Nano Banana 等自然语言图像模型的共同 Prompt 语义基线。

## 未采用的内容

- 不复制官方完整 system prompt；
- 不复制官方大段示例或原句；
- 不引入官方 checkpoint、模型权重或推理代码；
- 不把 Qwen 专属 JSON 字段强制用于所有模型；
- 不建立第二套 `references/models/` 目录，避免破坏仓库现有模型无关 Reference 架构；
- 不复制 iamyoki 项目的路由器、README、validator 或输出 UI 结构。

## 架构决策

正式运行真源放在：

`assets/templates/prompt-finalization-contract.md`

理由：

- 它是所有任务在最终交付前都会执行的运行输出合同，不属于某一具体业务 Task、Control、Library、Style 或 Diagnostic；
- 作为 output contract 不占业务 Reference 加载预算；
- 避免为 Qwen 单独建立模型目录，从而保持正式 Reference 的模型无关约束；
- Qwen 只作为规则来源和默认基线，目标模型专属语法仅在用户明确要求时最小适配。

## 版权与许可结论

Qwen 官方仓库当前许可证包含非商业研究限制，因此正式文件只保留独立重写后的抽象机制和仓库自身执行规则，不复刻原始系统提示词文本。iamyoki 项目为 Apache-2.0，可作为实现结构参考，但本次同样只做独立架构整合，不复制其完整 Skill 正文。
