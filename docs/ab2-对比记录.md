---
type: verify
id: verify.frontend-aesthetic.ab2
name: A/B 验证实验 2 · 氛围艺术风极光电台
status: active
updated: 2026-10-05
owner: <项目负责人>
stage: 05
---

# A/B 验证实验 2 · 卡 2（氛围艺术风）· 极光电台概念页

> 目的：验证卡 2（样本 001 Vesper）8 维指标能否让普通模型脱离训练均值。题材换新（极光电台概念页），排除题材偶然。
> 方法：A 版 = 一句话「用极光氛围艺术风做一个极光电台概念页」；B 版 = 注入卡 2 完整 8 维。

## 产物

| 版本 | 文件 |
|---|---|
| A 版（无指标） | `ab2-radio-no-constraints.html` |
| B 版（有指标） | `ab2-radio-constraints.html` |

## 对比结论

| 维度 | A 版（无指标） | B 版（有指标） |
|---|---|---|
| ② 色板 | **蓝紫色渐变**背景（#0b0e2a→#1a1040）+ 紫蓝霓虹渐变文字——「极光=紫色」是训练均值默认反应 | 近黑 #071315 + 薄荷绿 #39f9ab/#acffd5 + 蓝 #57b8ef，**刻意避开紫色**（样本 001 指标） |
| ① 字体 | Orbitron 科技感字体 + 渐变文字 | Georgia 巨型衬线 clamp(64px,9vw,145px) -5px 字距 + Arial 标签 3px 大字距 |
| ③ 网格 | 居中 hero + 三等分发光卡片 | max-width 1500 中心 + 双栏 1.5fr:1fr + 玻璃卡 18px 圆角 + 大留白 |
| ④ 动效 | 柱状图无意义脉冲 3s | 极光丝带 14s ease-in-out alternate 漂移 + 暂停/恢复按钮 + 柱状图生长 stagger + reduced-motion |
| ⑤ 背景 | 单层线性渐变 | 四层：径向渐变 + 模糊丝带（blur 65px）+ 星点阵 + 玻璃拟态（backdrop-filter 20px） |
| ⑦ 结构 | 标准 hero+卡片+图表+直播区模板 | header→巨型衬线标题（em 强调色）→intro→双栏（玻璃信息卡+活动柱状图+slider）→footer |
| ⑧ 可访问 | 无 aria | slider 标注；数据 illustrative 标注；aria-pressed（暂停按钮）；reduced-motion |

## 结论

1. **指标有效（复现）**：B 版完全脱离"紫色霓虹"均值，呈现 quiet Arctic night 气质；A 版完美落入均值（蓝紫渐变 + 发光卡片 + Orbitron）。
2. **「禁紫」禁区直接命中**：A 版证明「极光→紫渐变」是训练分布高频联想，卡 2 的"刻意避开紫色、用薄荷/蓝"是最强纠偏 token。
3. L1 量化：B 版字号梯度 64→145px（2.3x 起，clamp 上限 2.2x）；玻璃面板 18px 圆角；动效 14s 显式 + reduced-motion；A 版全不达标。
