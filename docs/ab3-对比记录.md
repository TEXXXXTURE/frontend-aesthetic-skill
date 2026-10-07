---
type: verify
id: verify.frontend-aesthetic.ab3
name: A/B 验证实验 3 · 建筑静默风山间石屋
status: active
updated: 2026-10-05
owner: A
stage: 05
---

# A/B 验证实验 3 · 卡 3（建筑静默风）· 山间石屋概念页

> 目的：验证卡 3（样本 004 Dune）8 维指标能否让普通模型脱离训练均值。题材换新（山间石屋概念页）。
> 方法：A 版 = 一句话「用建筑静默风做一个山间石屋概念页」；B 版 = 注入卡 3 完整 8 维。

## 产物

| 版本 | 文件 |
|---|---|
| A 版（无指标） | `ab3-house-no-constraints.html` |
| B 版（有指标） | `ab3-house-constraints.html` |

## 对比结论

| 维度 | A 版（无指标） | B 版（有指标） |
|---|---|---|
| ① 字体 | Georgia/宋体衬线标题 + 无字距处理 | Georgia 巨型衬线 clamp(50px,6.5vw,100px)/0.97 -4px 字距；logo 32px 8px 字距；标签层 9px + 2-3px 字距；specs 数字 26px Georgia |
| ② 色板 | 通用暖灰米白（#f2ede4/#3d362c/#8a7350），无角色结构 | 全土色系 10 色（沙 #e9dfcc / 墨 #40372c / 石灰蓝→奶油天空渐变 / 太阳 #fff2cd 光晕 / 土地 #c3a37f / 门 #372f24→#64523b）+ 夜间 filter |
| ③ 网格 | 居中 hero + 三卡片画廊占位 + 两栏 about/specs | **36%/64% 不对称分栏** + copy 大留白（10vh 3vw 40px 5vw）+ specs gap 30px |
| ④ 动效 | 仅按钮 hover | 场景 filter 1s 日光/暮光切换 + reduced-motion → transition:none |
| ⑤ 背景 | 纯色 + 占位色块（无图形） | 纯 CSS 建筑插画：太阳光晕（box-shadow 100px）/ 土地曲线（border-radius + rotate）/ 立方体+斜屋顶（skewX）/ 阴影（skewX 45deg），零图片 |
| ⑦ 结构 | 导航条+居中 hero+画廊+关于+页脚（模板） | header→编辑 intro（tiny 标签+巨型 h1+短文+按钮+specs）→大型 CSS 插画场景（太阳/土地/房屋/坐标注释）→footer |
| ⑧ 可访问 | 无 aria | role=img + aria-label（场景）；aria-pressed（日光切换按钮）；reduced-motion；语义标签 |

## 结论

1. **指标有效（第二次复现）**：B 版呈现"Architecture of Stillness"气质——不对称编辑式排版 + 手绘建筑插画 + 日光切换；A 版即使带"建筑静默风"方向词，结构仍是"导航+居中 hero+卡片"模板，只是色调素了些。
2. **CSS 插画是建筑静默风的灵魂**：A 版用占位色块，B 版用纯 CSS 画出太阳/山丘/石屋/阴影——这是「背景质感」维度把"零图片"约束转化为实际构图力的直接证据。
3. L1 量化：B 版字号梯度 50→100px（2x，clamp 上限 2x）+ 巨型 3x 需求未达（卡 3 本身梯度即 2x，属卡参数特性）；对比度 #40372c on #e9dfcc ≈ 11:1；网格 36/64 不对称。
