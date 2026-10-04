---
type: skill
id: skill.frontend-aesthetic
name: frontend-aesthetic-skill
version: 0.2
status: draft
updated: 2026-10-05
owner: A
origin: 前端审美 Skill 规划方案 v0.1（2026-10-04）；v0.2 = A/B 三连验证反哺禁区扩充（2026-10-05）
---

# 前端审美 Skill v0.1

> 一套把"万分之一审美"翻译成可执行约束的 Skill：从高审美样本提取 8 维 token 级指标 → 固化成约束网络 → 用户只给风格方向词 → Skill 展开 → 生成 → 量化闸门验收。可装载到任何 coding agent。

## 使用协议（对 coding agent）

```
用户输入: 风格方向词 + 内容需求
    ↓
模式判断: 探索态（放开约束给发散）/ 收敛态（锁死全部 8 维）
    ↓
卡匹配: 命中最接近的风格预设卡，套用其 8 维 token 级指标
    ↓
约束注入: 生成时 system prompt / CLAUDE.md 附加，8 维全覆盖不留缝隙
    ↓
产物自检: 按 8 维逐项自检清单核对产物，输出自检结果
    ↓
量化验收: L1 几何（8pt 网格/对比度/密度）→ L2 参考达成 → L3 人工
```

## 两档模式

| 模式 | 行为 | 适用 |
|---|---|---|
| 探索态 | 只给风格方向词 + 3-4 个关键维度（字体/色板/风格词），其余放开 | 创意发散、选方向 |
| 收敛态 | 8 维全锁死（token 级值域 + 白名单 + 禁区全注入） | 定稿生成、交付 |

## 8 维约束网络

1. **字体系统**：白名单（编辑风 Playfair/Fraunces · 代码风 JetBrains/Fira · 独特风 Bricolage，按风格卡锁定）；禁 Inter/Roboto/Arial 作 display；角色分配 display/body/mono 三分；配对高对比原则（衬线 display + 无衬线 body/元数据）
2. **色板角色表**：背景/表面/边框/正文/强调 五角色；主导色 + 锐利强调色（禁平均分配）；禁紫渐变白底；CSS variables 强制
3. **间距与网格**：8pt/4pt 网格遵守；网格列比显式（禁 1fr 平均分栏）；字距节奏统一（标签层大字距 / 巨型标题负字距）；clamp 字号梯度 3x+
4. **动效参数**：缓动区间显式（0.8-1.4s）；聚焦高影响时刻（stagger reveal/scroll scrub/功能切换）；禁跳动/闪烁/散乱 micro；尊重 reduced-motion
5. **背景质感**：多层渐变/几何图案/情境效果；禁纯色平铺；CSS 绘制零外部资产
6. **风格方向词**：一个词锁定气质；具象参考（IDE 主题/文化审美/印刷史/建筑）
7. **结构与内容**：页面区块显式清单；demo 数据必须"活"；虚构数据明确标注 illustrative
8. **可访问与交付**：语义 HTML/可见焦点/aria；60fps/pixel-ratio cap；输出完整不截断 + 自检清单

## 通用禁区（反均值出拳，任何风格卡都适用）

- 禁 Inter / Roboto / Arial 作 display 字体（Arial 仅可作 body/元数据，且需字距拉开）
- 禁紫色渐变 + 白底（训练分布最高频丑组合）
- 禁居中对称模板布局（一律不对称网格）
- 禁无差别大圆角卡片堆叠
- 禁纯色平铺背景（至少两层质感）
- 禁无参数动效（每个动画必须有显式时长/缓动/reduced-motion 降级）

### v0.2 新增禁区（A/B 三连验证 A 版反推，2026-10-05）

- 禁 **Playfair Display**（训练分布默认"高级感"衬线，与 Inter 组合 = 均值模板；ab1 A 版实证）
- 禁「主题 → 紫色」联想（极光 / 星空 / 宇宙 / 科技类题材默认紫渐变；ab2 A 版实证）
- 禁 **Orbitron** 类科技字体做 display（太空 / 科技题材均值反应；ab2 A 版实证）
- 禁无意义脉冲动画（只为"动"而动的动画；ab2 A 版实证）
- 禁图片占位符敷衍（视觉区至少用 CSS 几何构成填充，零图片前提下依然要有构图力；ab3 A 版实证）

---

## 预置风格预设卡

### 卡 1 · Swiss 印刷风（样本 002 FORM — 独立设计杂志封面）

| 维度 | 指标（token 级） |
|---|---|
| ① 字体 | Arial sans masthead 900 字重 -0.09em 字距 + Georgia serif 标题/正文；sans+serif 高对比配对；标签层统一 letter-spacing:2px |
| ② 色板 | 8 色全印刷色系：背景 #f2eee5 / 墨 #25231f / 强调朱红 #d63823 / 奶油 #efc6a4 / 深棕 #2e262b / 暗红 #b33020 / 红 #bc3729 / 灰 #ada79c |
| ③ 间距网格 | 三栏 1.1fr:1.7fr:0.8fr 不对称；巨型报头 clamp(90px,22vw,340px)；规则线 2px；标签字距 9-10px |
| ④ 动效 | 雕塑 hover 变换 rotate/skewY/border-radius 0.8s；reduced-motion 全尊重 |
| ⑤ 背景质感 | 纯色新闻纸 + CSS 雕塑构成（无图片）；几何抽象（圆环+方块+阴影） |
| ⑥ 风格词 | "Swiss masthead, newspaper rules, asymmetric grid, restrained print colors" |
| ⑦ 结构 | 报头→巨型刊名（O 字标红）→规则线→三栏（intro/art/sidebar）→折叠编辑信→页脚 |
| ⑧ 可访问 | aria-expanded、role=img、aria-label、reduced-motion |

### 卡 2 · 氛围艺术风（样本 001 Vesper — 极光观测站）

| 维度 | 指标（token 级） |
|---|---|
| ① 字体 | Georgia 巨型衬线标题 clamp(64px,9vw,145px)、-5px 字距、正常字重；Arial 正文/标签（3-4px 大字距）；衬线主标题+无衬线元数据配对 |
| ② 色板 | 近黑 #071315 底 + 薄荷绿 #39f9ab/#acffd5 + 蓝 #57b8ef 极光 + 玻璃 #d0f7e708 透明面板——刻意避开紫色，用薄荷/蓝 |
| ③ 间距网格 | max-width 1500px 中心；双栏 1.5fr:1fr；玻璃卡 18px 圆角；大留白 |
| ④ 动效 | 极光丝带 14s ease-in-out infinite alternate 漂移；暂停/恢复按钮；reduced-motion |
| ⑤ 背景质感 | 四层：径向渐变 + 模糊渐变丝带（blur 65px）+ 星点阵（mask-image）+ 玻璃拟态（backdrop-filter blur 20px） |
| ⑥ 风格词 | "quiet Arctic night, atmospheric instrument panel, monumental editorial typography" |
| ⑦ 结构 | header→巨型衬线标题（em 强调色）→intro→双栏（玻璃信息卡+极光活动柱状图+slider）→footer |
| ⑧ 可访问 | slider 标注；reduced-motion；数据标注 illustrative（防虚构） |

### 卡 3 · 建筑静默风（样本 004 Dune — 沙丘住宅概念页）

| 维度 | 指标（token 级） |
|---|---|
| ① 字体 | Georgia 衬线 display（logo 32px / 8px 字距；h1 clamp(50px,6.5vw,100px)/0.97、-4px 字距、normal 字重）；Arial 正文 13px/1.9、max-width 270px；标签层 9px + 2-3px 字距；specs 数字 26px Georgia + 9px 标签 |
| ② 色板 | 全土色系：沙 #e9dfcc 底 / 墨 #40372c / 土灰 #796c5b / 石灰蓝→奶油天空渐变 #cbd5cd→#ece0c6 / 太阳 #fff2cd+光晕 #fff3b9 / 土地 #c3a37f / 房屋 #d5c5a7→#eee0c7 / 门 #372f24→#64523b / 边框 #40372c33；夜间 filter brightness(.63) hue-rotate(325deg) |
| ③ 间距网格 | 36%/64% 不对称分栏；copy 10vh 3vw 40px 5vw 大留白；h1 margin 32px；specs gap 30px；标签-巨型标题-标签的节奏对比 |
| ④ 动效 | 场景 filter 1s 日光/暮光切换（单一功能向动效）；reduced-motion → transition:none |
| ⑤ 背景质感 | 纯 CSS 建筑插画：太阳光晕（box-shadow 100px 模糊）/ 土地曲线（border-radius 50% 60% + rotate -7deg）/ 立方体+斜屋顶（skewX -25deg）/ 阴影（skewX 45deg）；多层 linear-gradient；零外部资产 |
| ⑥ 风格词 | "Architecture of Stillness" / "sand, limestone, sage sky, generous whitespace and fine serif typography" |
| ⑦ 结构 | header（logo+tagline）→编辑 intro（tiny 标签+巨型 h1+短文+按钮+specs）→大型 CSS 插画场景（太阳/土地/房屋/坐标注释）→footer |
| ⑧ 可访问 | role=img + aria-label（场景）；aria-pressed（按钮状态）；reduced-motion；语义 header/main/section/footer；响应式断点 700px |

---

## 产物自检清单（8 维逐项，生成时随产物输出）

- [ ] ① 字体：display 未用 Inter/Roboto/Arial；白名单字体已用；衬线/无衬线配对成立；标签层字距拉开
- [ ] ② 色板：CSS variables 已用；背景/表面/边框/正文/强调五角色齐全；主导色+强调色结构成立；无紫渐变白底
- [ ] ③ 间距网格：8pt/4pt 网格遵守；列比显式且不对称；字号梯度 ≥3x（clamp）
- [ ] ④ 动效：每个动画有显式时长/缓动；区间 0.8-1.4s；无跳动/闪烁；reduced-motion 已降级
- [ ] ⑤ 背景质感：至少两层质感（渐变/几何/情境）；非纯色平铺；零外部资产
- [ ] ⑥ 风格词：页面气质与目标风格词一致（视觉自检）
- [ ] ⑦ 结构：页面区块清单显式；demo 数据"活"；虚构数据已标 illustrative
- [ ] ⑧ 可访问：语义标签/aria 状态/可见焦点/reduced-motion 全通过

## 量化验收（L1 几何，可测）

- 8pt/4pt 网格遵守度（间距采样均落在网格上）
- 对比度（正文/背景 ≥ 4.5:1，WCAG AA）
- 密度（信息区块数量与留白比例）
- 字号梯度（最大/最小 ≥ 3x）
- 动效参数合规（时长/缓动/reduced-motion 存在性）

## 附：验证记录（指标有效性证据链）

三组 A/B 验证（2026-10-04~05，普通模型执行，同题材无指标 vs 有指标）：

| 实验 | 卡 | 题材 | 结论 |
|---|---|---|---|
| ab1 | 卡 1 Swiss 印刷风 | 咖啡馆首页 | ✅ 指标显著有效 |
| ab2 | 卡 2 氛围艺术风 | 极光电台 | ✅ 复现有效（禁紫命中均值） |
| ab3 | 卡 3 建筑静默风 | 山间石屋 | ✅ 二次复现有效 |

> 共性结论：三张卡、三个题材，B 版全部脱离训练均值、A 版全部落入均值（即使带方向词）——**方向词不足是普遍现象，token 级约束是杠杆**。详细记录在项目总仓 `05-验证记录/`（ab1/ab2/ab3 + 测试记录.md）与产品仓 `ab/`。

## 附：样本来源

- 样本 001/002/004：MiaAI-Lab/GPT-6-Astra-100-HTML-Files（https://github.com/MiaAI-Lab/GPT-6-Astra-100-HTML-Files）——GPT-6 Astra 生成的高审美单文件 HTML
- 8 维框架归纳依据：Claude cookbook《Prompting for frontend aesthetics》+ OpenAI GPT-6 Astra 发布页 + 三样本全码解剖
