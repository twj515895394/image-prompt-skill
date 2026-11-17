# Cinematic Styles

当任务需要影视叙事画面、电影照明、镜头质感、类型片气质或导演式视觉时读取本分类。

## 电影剧照与影视叙事画面

当用户要求电影剧照、类型片单帧、影视封面，或需要把“电影感”落实为事件瞬间、摄影位置、光影、色彩、景深和情绪关系时，读取：

- `film-still-language.md`
## MJ 柔雾 / 梦境电影风格体系

当用户要求 MJ 氛围底图、写实奶油柔光、写实灰雾电影、梦境艺术电影或半写实 3DCG 电影视觉，需要自动识别 A–D 风格时，读取：

- `mj-atmospheric-film-look.md`

普通叙事电影剧照仍优先 `film-still-language.md`。两者都是 style 叶子，单次按任务主问题只选一份，保持 0–1 style 预算。

## 边界

- 本目录保存电影视觉如何实现；
- 具体景别、机位、焦段和景深判断归入 `../../controls/composition-camera/`；
- 具体光源、阴影和主体分离归入 `../../controls/lighting-color/`；
- 具体电影色调方案归入 `../../libraries/lighting-color/`；
- 人物、场景和道具选项归入 libraries；
- 本索引不承载具体风格正文。