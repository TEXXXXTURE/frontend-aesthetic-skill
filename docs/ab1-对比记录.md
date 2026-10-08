---
type: verify
id: verify.frontend-aesthetic.ab1
name: A/B 验证实验 1 · Swiss 印刷风咖啡馆首页
status: active
updated: 2026-10-04
owner: <项目负责人>
stage: 05
---

# A/B 验证实验 1 · 8 维指标对普通模型的影响

> 目的（用户指定）：验证「从高审美样本提取的 8 维 token 级指标」能否让普通模型脱离训练均值分布，做出高审美前端。
> 实验设计：同一题材（Swiss 印刷风 · 咖啡馆首页），A 版只给一句话方向词（无指标），B 版注入卡 1 完整 8 维指标。执行模型：普通模型（非 Opus 5.5 / GPT-6 级）。

## 产物

| 版本 | 文件 | 生成条件 |
|---|---|---|
| A 版（无指标） | `ab/ab1-cafe-no-constraints.html` | 仅一句话：「用 Swiss 印刷风格做一个咖啡馆首页」，完全凭自然能力生成 |
| B 版（有指标） | `ab/ab1-cafe-constraints.html` | 同题材 + 注入样本 002 FORM 的 8 维 token 级指标（SKILL.md 卡 1） |

## 8 维逐项对比

| 维度 | A 版（无指标） | B 版（有指标） | 差异来源 |
|---|---|---|---|
| ① 字体 | Playfair Display 标题 + Inter 正文（训练分布 TOP 组合）；hero 无字距处理 | Arial 900 masthead -0.09em + Georgia serif 正文；标签层统一 letter-spacing:2px | 字体白名单 + 角色分配 + 负字距指标 |
| ② 色板 | 米白 #faf8f5 + 黑 #1a1a1a + 棕金 #c98a4b（"瑞士"触发的通用暖调）；无角色表 | 8 色全印刷色系（#f2eee5/#25231f/#d63823/#efc6a4/#2e262b/#b33020/#bc3729/#ada79c）；五角色齐；O 字标红 | 色板角色表 + 主导/强调结构 |
| ③ 间距网格 | 居中对称；max-width 1100 容器；三卡片 1fr 等分；hero 居中 | 三栏 1.1fr:1.7fr:0.8fr 不对称；巨型刊名 clamp(90px,22vw,340px)；2px 规则线全页贯通 | 网格列比显式 + 不对称 + 字号梯度 3x+ |
| ④ 动效 | 仅按钮 hover 变色 0.3s（无显式参数意识） | 雕塑 hover 变换 0.8s cubic-bezier（rotate/skewY/border-radius）；reduced-motion 全降级 | 动效参数区间显式 + reduced-motion |
| ⑤ 背景质感 | 纯色 + 简单渐变；照片占位符（无实际图形） | 新闻纸纯色 + 纯 CSS 几何构成（圆环杯口/奶油杯身/杯碟/豆子/阴影），零图片零依赖 | 背景质感 ≥2 层 + CSS 绘制零外部资产 |
| ⑥ 风格词 | 只做出"编辑感 tagline + 衬线标题"的皮毛 | "Swiss masthead, newspaper rules, asymmetric grid, restrained print colors"气质完整成立 | token 级风格词 vs 模糊方向词 |
| ⑦ 结构 | 标准模板：导航条+hero+三卡+深色菜单区+关于+页脚 | 报头→巨型刊名→规则线→三栏（intro/art/sidebar）→折叠编辑信→页脚 | 页面区块显式清单 |
| ⑧ 可访问 | 无 aria；仅 hover 变色 | role=img + aria-label（场景/区块）；aria-expanded（折叠编辑信，已补）；focus-visible；reduced-motion。B 版无交互按钮，故无 aria-pressed 需求 | 可访问维度强制 |

## 结论

1. **指标有效（显著）**：B 版完全脱离模板均值，呈现"瑞士印刷杂志"气质；A 版即使带着"Swiss 印刷风"方向词，仍落入训练分布均值（居中布局、Playfair+Inter、圆角卡片、通用暖色）。
2. **方向词不够，token 级约束才是杠杆**：A 版证明"好形容词"无法拽离均值（官方 cookbook 结论在普通模型上复现）；B 版证明"色名/字重/列比/字距/禁区"可直接执行。
3. **最关键的 3 个维度**（肉眼对比差异最大）：色板角色表（摆脱通用暖色）、不对称网格（摆脱居中模板）、字体白名单+字距（摆脱 Playfair+Inter 组合）。
4. **L1 量化可测**：B 版字号梯度 90→340px（3.7x，达标）；对比度 #25231f on #f2eee5 ≈ 12:1（远超 WCAG AA 4.5:1）；网格列比 1.1/1.7/0.8 非平均；A 版全部不达标。

## 局限与下一步

- 单一样本、单一题材、单一执行模型——需要扩大验证矩阵（其余预设卡 + 不同题材）才能排除偶然。
- 未做 L2（参考达成度比对：B 版 vs 样本 002 源码逐 token 对齐度）与 L3 人工评审（owner 主观判定）。
- 2026-10-05 复核补漏：B 版 ⑧ 维度 aria-expanded 原未显式实现（原生 details 语义可访问但不写显式属性），已补 summary aria-expanded 初始态 + toggle 事件同步，并重新渲染验证无破坏。aria-pressed 因 B 版无交互按钮不适用，如实记录。
- 下一步建议：用卡 2/卡 3 各做一组 A/B；对 B 版跑 L2 参考比对脚本。
