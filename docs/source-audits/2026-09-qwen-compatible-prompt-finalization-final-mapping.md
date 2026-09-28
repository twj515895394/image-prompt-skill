# 2026-09 Qwen-Compatible Prompt Finalization Final Mapping

## 来源到正式运行文件的映射

| 来源机制 | 最终去向 | 处理方式 |
|---|---|---|
| Qwen T2I observer-style description | `assets/templates/prompt-finalization-contract.md` | 抽象为模型无关的 T2I 最终化规则 |
| Qwen T2I spatial walk / material / lighting / text literalness | `assets/templates/prompt-finalization-contract.md` | 重新组织为通用自然语言 Prompt 语法 |
| Qwen Edit attribute disentanglement | `assets/templates/prompt-finalization-contract.md` | 抽象为局部编辑与多图合成的最终表达规则 |
| Qwen image reference role / canvas logic | `assets/templates/prompt-finalization-contract.md` | 与现有 multi-image reference 语义衔接，只保留最终表达层职责 |
| Qwen wh_ratio / ratio_follow | `assets/templates/prompt-finalization-contract.md` | 仅保留在用户明确要求 Qwen 结构化输出时 |
| iamyoki skill routing implementation | 未进入正式运行正文 | 只作为实现结构参考，不建立第二套路由器 |
| iamyoki validator | 未复制 | 现有仓库继续使用自身完整性检查；新增 QC 为运行时语义检查 |

## 现有文件更新

- `SKILL.md`
  - 增加 Prompt Finalization 固定运行阶段；
  - 将最终语言与表达从“默认中文”改为由 Finalization Contract 决定；
  - 增加 QC、自动修复和复检硬门禁；
  - 明确 Qwen-compatible 为默认跨模型语义基线。

- `assets/templates/mode-quick-output-contract.md`
  - 快速模式输出前强制 Finalization + QC + 自动修复；
  - QC 过程不对外展示；
  - 结构化请求不重复输出 Prompt。

- `assets/templates/mode-interactive-output-contract.md`
  - 仅在最终收口时执行 Finalization + QC + 自动修复；
  - 交互设计过程不提前套最终语法。

- `scripts/check_reference_integrity.py`
  - 将 `assets/templates/prompt-finalization-contract.md` 增加为 required architecture path。

- `references/SOURCES.md`
  - 登记 Qwen 官方规范和 iamyoki Skill 来源、许可边界及正式落点。

## 未创建的目录

没有创建：

```text
references/models/
references/qwen/
references/gpt-image/
```

原因：正式 Reference 保持模型无关，模型差异只在最终输出表面格式层处理。

## 最终架构位置

```text
Input
→ Task
→ Controls / Libraries / Styles
→ Visual Intent Assembly
→ Prompt Finalization Contract
→ QC
→ Auto Repair
→ QC Re-check
→ Quick / Interactive Output Contract
```

## 清理结论

本批次没有导入第三方原始文档、图片、模型文件或完整 Prompt 数据集，因此不存在需要长期保留的 `source-staging` 原始资料。来源通过 URL + source audit 追溯，正式运行层只保留独立重写后的抽象规则。
