# Assets

当前目录保存可直接复用的交付模板。模板只定义输出字段、顺序和排版，不承载任务知识。

## 任务模板

- `templates/finished-image-template.md`
- `templates/image-to-image-template.md`
- `templates/image-editing-template.md`
- `templates/prompt-reverse-engineering-template.md`
- `templates/character-assets-template.md`
- `templates/scene-assets-template.md`
- `templates/storyboard-assets-template.md`
- `templates/video-reference-frames-template.md`

## 使用规则

- 普通短任务不强制读取模板
- 用户要求完整、结构化交付时才读取
- 每次只读取当前任务对应的一份模板
- 快速模式与交互模式共用同一任务模板
- 模式差异通过“自动补全项”或“方向决策摘要”等字段体现
