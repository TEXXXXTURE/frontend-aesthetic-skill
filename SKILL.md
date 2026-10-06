---
type: skill
id: skill.frontend-aesthetic
name: frontend-aesthetic-skill
version: 0.4
status: draft
updated: 2026-10-07
owner: A
origin: 前端审美 Skill 规划方案 v0.1（2026-10-04）；v0.2 = A/B 三连验证反哺禁区扩充（2026-10-05）；v0.3 = 新增卡 4 Munder 像素办公室风（2026-10-07，样本 005 源码解剖）；v0.4 = 色板维度升级为「用色逻辑」（四层模型 + 提取规范 + 卡 4 重写样板，2026-10-07）
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
2. **用色逻辑**（v0.4 起取代"色板角色表"）：提取目标从"色值快照"升级为"用色逻辑"——①角色表（背景/表面/边框/正文/强调 五角色 + 状态语义色）②关系规则（饱和度带/明度带/对比度约束，可量化）③示例锚点色值（**仅作参考样例，非硬约束**）；禁平均分配；禁紫渐变白底；CSS variables 强制。提取方法见「用色逻辑提取规范」
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

## 用色逻辑提取规范（v0.4 新增）

> 提取颜色时，目标不是"这页用了哪些色值"，而是"**这个设计师的用色脑子里在想什么**"——协调感来自用色逻辑，不来自具体色值。色值可换，逻辑不变，页面依然协调；反过来只抄色值换题材就废。

### 为什么必须从源码提取

用色逻辑写在源码里，视觉模型（看截图）只能看到"有什么颜色"，看不到"为什么是这些颜色"：

| 信息层 | 视觉模型 | 源码提取 |
|---|---|---|
| 用了什么色值 | ✅ | ✅ |
| 颜色在系统里的角色（变量名 `--cth-coral`、`--cth-status-thinking`） | ❌ | ✅ |
| 颜色间的关系规则（注释"强调色落在 Linear/Radix 的 calm band"） | ❌ | ✅ |
| 对比度约束（注释"ink-300 现在是 3.12-3.59:1"） | ❌ | ✅ |
| 使用频次/用途（ink-300 用 187 次、93 次做边框） | ❌ | ✅ |

### 用色逻辑四层模型

| 层 | 内容 | 可迁移性 |
|---|---|---|
| L0 色值 | `#D96A62` | 不可迁移，会过时 |
| L1 角色表 | coral=强调/危险、status-thinking=思考中 | 可迁移（换色值保留角色） |
| L2 关系规则 | 强调色低饱和带、文字对比度 ≥4.5:1、暗色地面亮度 0.009-0.020 | **可迁移（协调感的来源，核心）** |
| L3 生成约束 | 双主题切换、禁用态专用色、状态=语义色 | 可迁移（系统行为） |

提取产物 = L1 角色表 + L2 关系规则 + L3 生成约束；L0 只作为「示例锚点色值」记录，标注"非硬约束"。

### 分辨物体色 vs 背景色（三道线索）

1. **变量命名编码角色**：`--cth-cream-50`（surface 层）、`--cth-ink-900`（文字层）→ 背景/表面；画中物体色往往是内联值或独立命名
2. **使用位置**：`background: var(--cth-cream-100)`（面板表面）vs 具体元素填充
3. **注释**：源码常直接说"这是地面""这是天空渐变"

**终极判据（可替换性测试）**：改掉这个色值——气质变但页面成立 → 风格色（进逻辑）；改掉就失真（沙变蓝）→ 物体色（记录物名，不进逻辑）。物体色由现实给定、不构成设计逻辑，**自然出局**。

### 提取产物格式

```
② 用色逻辑
├── 角色表：五角色 + 状态语义色（换色值保留角色）
├── 关系规则：饱和度带 / 明度带 / 对比度约束（可量化）
└── 示例锚点色值（非硬约束）：仅作参考样例
```

生成时注入"逻辑（约束）"，agent 据题材**推导**具体色值，不抄锚点。

---

## 预置风格预设卡

> **卡 1-3 状态：v0.4 色板维度已升级为「用色逻辑」，但卡 1-3 的 ② 行仍为旧格式「色值快照」，待按新规范回标**（拆分角色表 / 关系规则 / 示例锚点，剔除物体色）。卡 4 已按新规范重写，为现行样板。

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

### 卡 4 · 像素办公室风（样本 005 Munder Difflin — AI Agent 可视化工作台）

> 样本：HarnessMD/munder-difflin（Electron + Pixi.js 的 AI Agent 可视化工作台，2026-10-07 前端源码解剖：tokens.css / themeRegistry.ts / PixelButton.tsx / fonts.css / 官方设计博客）。**桌面工具 UI 类**——区别于卡 1-3 的落地页类：场景层（Pixi 办公室）与 UI 层（面板/看板/终端）双轨并存。A/B 验证待补（本卡源自真实产品源码，非 GPT 样本）。**v0.4 已按「用色逻辑」新规范重写 ② 行，为现行样板**。

| 维度 | 指标（token 级） |
|---|---|
| ① 字体 | 三角色显式分工：display="Press Start 2P"（仅品牌小标签，8-16px 大字距，不承载正文）+ ui="Inter"（400-700 可变，全部可读文本）+ mono="JetBrains Mono"（代码/终端）；CJK 走系统面 fallback 链（PingFang SC → Microsoft YaHei → Noto Sans CJK SC）；三字体自托管 woff2 内置，零外部字体依赖；display 档字号 16/12/8px，body 16/14/13px，行高整数倍（24/20/18/12） |
| ② 用色逻辑 | **角色表**：背景/表面（cream-50→paper-200 纸面系）、边框（ink-300 发丝线）、正文（ink-900/700/500 墨系三档）、强调（六色系 coral/mint/sky/lemon/lilac/peach + 各带 -light 填充体）、状态（10 种语义色 idle/thinking/working/waiting/blocked/success/ghost/compacting/looping/typing，**颜色承载状态信息**）。**关系规则**：①强调色**低饱和带**——六色同处一个饱和度区间（注释原话：原版全饱和街机色"read as noise at UI density"，v0.3.4 校准到 Linear/Radix 的 calm band）②对比度=工程——双主题逐值 WCAG 验证：正文 ≥4.5:1、边框 ≥3.0:1、暗色地面非纯黑（亮度 0.009-0.020，注释："NOT BLACK, AND NOT WHITE"）、暗色文字暖白（0.71 而非 0.84）③结构来自表面对比非轮廓（发丝线边框，注释："structure now comes from surface contrast, not outlines"）④CSS variables 强制。**示例锚点（非硬约束）**：cream-50 #FFFDF5 / ink-900 #1A1320 / coral #D96A62 / sky #4F9FAF / 暗色地面 #17171B / 暗色文字 #DEDBD6 |
| ③ 间距网格 | 8pt 体系（4/8/12/16/24/32/48/64）；控件高度 8pt 对齐（按钮 sm 24 / md 32 / lg 40，padding 8/12/16）；面板边框 = inset 0 0 0 1px 发丝线（结构来自表面对比，不来自轮廓）；**硬阴影无模糊** 3px 3px 0 rgba(26,19,32,.14)（明）/ 4px 4px 0 rgba(0,0,0,.45)（暗）——像素感深度，非弥散阴影；禁用态文字专用 ink-500（双主题兼容） |
| ④ 动效 | 按钮按压 = translateY(1px) + inset 1px 边框（物理下沉，非变色）；信封飞行 = 二次贝塞尔弧（中点正弦抬升）+ ease in/out + 到达 burst ring；角色四态 walk/type/read/idle（真实事件驱动，非脚本循环）；相机平滑 lerp 跟随 + 地图边缘钳制；单共享 ticker 驱动全场景（帧预算可预测）；像素渲染 antialias:false + roundPixels:true + nearest 缩放（硬像素边，无模糊） |
| ⑤ 背景质感 | 场景层 = Tiled 地图（.tmj）16×16 瓦片集（office-tileset / a5 floors-walls / interiors 三图集按 firstgid 排布）；办公室叙事道具：CEO 办公室（godOnly：植物+雪茄 18s）、咖啡经济闭环（托盘→咖啡机→水槽→托盘，maxCups 4）、饮水机/冰箱/货架/垃圾桶/浇花/窗风痕；交互道具锚点：日历→TRIGGERS、看板→TASKS、时钟→CLOSING TIME；零外部资产 |
| ⑥ 风格词 | "pixel-art crisp, hard-shadow chrome, low-saturation product palette, a workplace you can watch"（The Office 喜剧致敬 × 开发工具里的游戏技术；位置/运动即状态，非装饰） |
| ⑦ 结构 | 双层结构：场景层（tile map + character layer + envelopes 共用一个 world 容器 + 相机变换）+ UI 层（CommandCenter：Floor/Terminal/Activity/Tasks/Triggers/Handbook 分页）；每个位置/运动映射真实事件：PreToolUse→走向工具站、PostToolUse→回位、Stop→桌面 idle、消息→信封按 speech act 着色（ask 冷色 / agree 暖色 / refuse 红 / escalation 特殊色）；角色同底稿调色盘区分（skin/hair/shirt 配方） |
| ⑧ 可访问 | 双主题 WCAG 逐值验证（正文 ≥4.5、边框 ≥3.0）；禁用态专用文字色（非变体继承）；reduced-motion 尊重；CJK/阿拉伯走系统面（中文 locale 专门适配，字体自托管解决大陆访问）；语义 HTML/aria/可见焦点；60fps 帧预算（单 ticker + 相机单节点变换 + nearest 缩放） |

---

## 产物自检清单（8 维逐项，生成时随产物输出）

- [ ] ① 字体：display 未用 Inter/Roboto/Arial；白名单字体已用；衬线/无衬线配对成立；标签层字距拉开
- [ ] ② 用色逻辑：CSS variables 已用；背景/表面/边框/正文/强调五角色齐全；关系规则落地（饱和度带/明度带/对比度约束可量化）；色值由逻辑推导而非抄锚点；无紫渐变白底
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
- 样本 005：HarnessMD/munder-difflin（https://github.com/HarnessMD/munder-difflin）——Electron + Pixi.js 的 AI Agent 可视化工作台；卡 4 由前端源码解剖提取（tokens.css / themeRegistry.ts / PixelButton.tsx / fonts.css / design 博客 / visualizing-ai-agents-pixijs + building-an-ai-office-floor），**桌面工具 UI 类首张卡，A/B 验证待补**
- 8 维框架归纳依据：Claude cookbook《Prompting for frontend aesthetics》+ OpenAI GPT-6 Astra 发布页 + 三样本全码解剖
