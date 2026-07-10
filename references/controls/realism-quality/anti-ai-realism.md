# 去 AI 感与真实照片控制

## 用途

当用户要求“看不出是 AI”“像真实照片”“像手机或相机真实拍出来”时，用具体拍摄关系、真实材质和合理不完美压制合成感、摆拍感和商业精修感。

## 何时读取

- 真人或生活场景需要真实照片感
- 用户明确反感塑料皮、假景深、过度精修
- 图生图需要把棚拍、网红写真改为自然纪实
- 办公室、街头、家庭等普通空间需要可信感

## 核心规则

真实感不是反复堆 `photorealistic`，而是以下关系同时成立：

- 拍摄者确实能站在那个位置
- 光线有明确且可信的来源
- 皮肤、布料和环境材质保留自然纹理
- 构图允许轻微但合理的不完美
- 场景存在真实使用痕迹和空间层次
- 主体像处在事件中，而不是专门配合镜头摆姿势

## 优先控制变量

### 拍摄来源

根据场景明确：

- 手机随手记录
- 会拍照的人用手机抓拍
- 微单自然抓拍
- 同事、朋友、同行者或路人视角

“谁在什么位置拍”比单写“纪实感”更有效。

### 真实材质

优先补：

- 轻微皮肤纹理，不过度磨皮
- 局部明暗和肤色并非完全均匀
- 布料自然褶皱、拉力和穿着痕迹
- 普通环境反射
- 真实空气感和前中后景层次

### 合理不完美

允许：

- 主体略偏画面一侧
- 轻微裁切或前景遮挡
- 背景不完全干净但信息可控
- 普通顶灯、窗光或环境反射造成的色温差

真实不等于故意降低画质，也不等于杂乱无重点。

## 更稳的 Prompt 写法

不要只写：

```text
photorealistic, masterpiece, 8k, perfect skin
```

优先写：

```text
像真实工作日中被同事用手机顺手记录的瞬间，非摆拍，主体没有刻意正对镜头，保留轻微皮肤纹理和布料褶皱，普通环境光形成自然明暗差，构图略有偏移但可信，背景保留真实使用痕迹，不过度磨皮，不过度虚化
```

## 慎用词

以下词容易把普通真实场景推向合成、海报或商业精修：

- masterpiece
- best quality
- ultra detailed
- 8k
- unreal engine
- perfect skin
- flawless face
- cinematic masterpiece
- award-winning photography

不是绝对禁止，而是不能依赖这些词建立真实感。

## 负向约束

只选择当前最危险的 2–4 组：

- no AI look
- no CGI
- no plastic skin
- no beauty filter
- no over-retouching
- no glamour studio shot
- no ad-like composition
- no fake bokeh
- no wax texture

## 联动关系

- 抓拍构图：`../composition-camera/candid-composition-imperfections.md`
- 办公室纪实：`../composition-camera/office-candid-camera.md`
- 普通办公室混合光：`../lighting-color/office-mixed-light.md`
- 生活化摄影表现：`../../styles/photography/lifestyle-candid-photography.md`

## 常见失败与修复

- 把真实理解成低清：恢复清楚主体，只保留自然纹理和曝光差
- 负向词很多但画面仍假：补拍摄者站位、动作阶段和环境证据
- 抓拍变成偷窥：改成同事、朋友或同行者的合理在场视角
- 纪实变成废片：保留第一视觉落点，不让不完美压过主体

## 校验

删除所有质量大词后，主体、场景、镜头、光线和材质仍然像一张现实中能够拍到的照片，才算控制成立。
