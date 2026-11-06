---
name: readme-orchestrator
description: |
  Intelligent README Design & Audit Orchestrator. Invoke whenever the user asks to "write a README", "beautify README", "make an interactive/aesthetic README", "redesign repo homepage", or "audit README". Automatically scans the repository, resolves style conflicts across 5 installed specialist README skills (beautify-github-readme, readme-styling, readme-generator-visual, github-readme, readme-rubric-audit), selects the optimal visual archetype (Project-Native SVG/Hybrid, Retro-Terminal Bitmap ASCII, Interactive GFM Media/Gallery, or Clean SDK/Library), executes the build, and runs a 100-point rubric + asset audit before delivery. Triggers: write readme/beautify readme/interactive readme/aesthetic readme/美化README/写README/设计README/readme skill/audit readme.
---

# README Orchestrator — 智能 README 视觉与交互总控台

## 为什么用总控路由（Orchestrator）而非单文件大杂烩

本机已安装的 5 个顶级 README Skill 各自代表不同的美学流派，存在**天然指令互斥**（例如 `readme-styling` 强制要求 74 列 ASCII 像素字符画头图，而 `github-readme` 明文禁止 ASCII 头图、主张 `<picture>` 亮暗自适应图；`beautify-github-readme` 则主推 1200px 矢量 SVG / AI 抠图合成海报）。
如果把 5 个技能硬塞进同一个单文件，Agent 会因规则打架产出四不像。本总控台采用 **Router → Specialist → Gate Audit** 三段架构：**按需加载唯一主视觉引擎 + 通用 GFM 交互容器 + 终检审计器**。

---

## 标准执行工作流（4 步闭环，含输入/输出）

1. **Step 1：仓库特征快扫与意图分类（Repo Signal Scan）**
   - **输入**：目标项目目录与用户一句话需求。
   - **动作**：读取目录结构、`package.json`/`pyproject.toml`/`Cargo.toml`、现有 `README.md` 及存量图片/视频资产（如 `assets/`、`promo/`、`product-card/`）。
   - **输出**：判定任务模式（`新建/重设计 Whole-README` ｜ `仅做视觉资产 Asset-Only` ｜ `仅评分审计 Audit-Only`）与项目基因（CLI/终端工具 ｜ AI/Web 视觉产品 ｜ SDK/算法库 ｜ 知识库/研究集）。

2. **Step 2：智能流派路由（Smart Skill Routing — 严禁同时加载冲突流派）**
   - **输入**：Step 1 的项目基因与用户偏好。
   - **动作**：按下表选择 **1 个主视觉流派 Skill** + **1 个交互容器规范（`github-readme`）**，读取对应 `SKILL.md`：

| 场景 / 用户偏好 | 选定的主视觉 Skill（只读 1 个） | 叠加的交互增强层 | 典型产出形态 |
|---|---|---|---|
| **A. 想要项目原生 SVG 海报 / AI 抠图合成 Hero / 精致章节头** | `~/.config/magpie/library/skills/beautify-github-readme/SKILL.md` | `github-readme`（`<picture>` 亮暗切换 + `<details>` 折叠） | 1200px 矢量 SVG Hero、Hybrid 角色/产品海报、SVG 章节横幅、可选动图 GIF |
| **B. 想要极客终端风 / 74 列像素块状字 / ASCII 逻辑门禁图** | `~/.config/magpie/library/skills/readme-styling/SKILL.md` | `github-readme`（`[!IMPORTANT]` 告警 + 表格面板） | `<!-- architect-team:readme-theme=midnight -->`、ASCII 大横幅、`█▓▒░` 渐变分割线、`▣ GATE` 路由图、`▰` 时间轴 |
| **C. 从零扫描代码库快速出带动态波浪头图 + 架构图的现代 README** | `~/.config/magpie/library/skills/readme-generator-visual/SKILL.md` | `markdown-mermaid-writing`（23 种 Mermaid 图表） | Capsule-render 动态渐变头图、分层 `shields.io` 徽章栏、Mermaid 架构图、仓库健康计分卡 |
| **D. 已有宣传片（MP4/GIF）/ 产品卡 / 截图，要做交互式多媒体画廊** | `~/.config/magpie/library/skills/github-readme/SKILL.md` | `readme-styling`（仅借用分割条与逻辑图） | 顶置 `<video>` + `<10MB` 16:9 GIF 双保险内嵌、`for-the-badge` 胶囊 CTA、2×2 `<table>` 关键帧画廊、`<details>` 交互抽屉 |
| **E. 只想给现有 README 打分挑刺与修 Bug** | `~/.config/magpie/library/skills/readme-rubric-audit/SKILL.md` | `beautify-github-readme/scripts/audit_readme.py` | 100 分六维体检报告（Identity/Trust/Onboarding/Structure/Craft/Agent）+ 断链修复清单 |

3. **Step 3：🔴 CHECKPOINT 冲突消解与构建落盘**
   - **输入**：选定流派的规则与项目真实数据。
   - **动作**：
     - 若用户同时想要「终端位图风 + 视频/图片画廊」（复合旗舰模式，如 `ai-creators-on-x`）：以 **流派 B（74 列 ASCII Banner + `█▓▒░` 分割线 + `▣` 逻辑图）** 为骨架，嵌入 **流派 D（`<picture>` 头图 + `<video>`/GIF 横屏内嵌 + `<table>` 2×2 画廊 + `<details>` 折叠卡）**。
     - **🛑 STOP 涉及 git commit / push / 覆盖非 README 业务代码时，必须先获用户确认**。
   - **输出**：写入 `README.md` 及配套视觉资产。

4. **Step 4：双引擎自动终检（Dual Verification Gate）**
   - **输入**：落盘后的 `README.md`。
   - **动作**：
     1. 运行静态资产与 SVG 检查脚本：
        ```bash
        python "C:/Users/xiaohanchen/.config/magpie/library/skills/beautify-github-readme/scripts/audit_readme.py" README.md
        ```
     2. 对照 `readme-rubric-audit/references/checklist.md` 自检首屏 10 秒可读性、安装命令可复制性与徽章真实性。
   - **输出**：`audit_readme.py` 零报错通过证明 + 最终预览。

---

## 检查点与失败恢复表（先读）

- 🔴 **CHECKPOINT 1（流派冲突拦截）**：绝不允许在同一份 README 中既按 `github-readme` 删掉 ASCII 头图、又按 `readme-styling` 强加 ASCII 头图——Step 2 必须明确声明本次采用的主流派（A / B / C / D / B+D 旗舰混合）。
- 🔴 **CHECKPOINT 2（视频内嵌兼容性门禁）**：凡要求在 README 中内嵌视频，**必须同时生成 `<10MB` 的 16:9 横屏 MP4（带 `-movflags +faststart`）与 `<10MB` 的 16:9 横屏 GIF**，并用 `<video>` + `<a href="video.mp4"><img src="preview.gif"></a>` + `![[mp4]]` 三合一写法通杀 GitHub / VS Code / Obsidian。

| 触发条件（如果 X 失败/异常） | 一线修复动作（先执行 Y） | 仍失败兜底（Fallback Z） |
|---|---|---|
| `audit_readme.py` 报 `missing image: ...` | 检查正文中是否有未转义的示例文本 `!<alt>[<img-src>]` 或断链路径，将其替换为普通文字或修复相对路径 | 移除损坏的图片引用，改用代码块或表格承载该信息 |
| GitHub 端不渲染内联 `<video>` 标签或 SVG 内部动画 | 自动降级到紧随其后的 `<a href="./promo/out/promo-readme.mp4"><img src="./promo/out/promo-readme.gif" width="100%"></a>` 可点击 16:9 动图 | 使用 `<table>` 2×2 高清静帧画廊并配跳转链接 |
| 用户未说明想要哪种视觉风格 | 展示 A（SVG 视觉故事）、B（终端位图极客风）、D（多媒体交互画廊）、B+D（全满贯旗舰风）4 个选项；若用户说「你定/看着办」，默认采用 **B+D 全满贯旗舰风** | 默认生成结构最稳的流派 D + B 组合 |

---

## 反例与黑名单（禁止动作）

| 编号 | 禁止动作（不要做什么） | 为什么禁止 | 强制替代做法 |
|---|---|---|---|
| **BL-1** | **禁止把整篇 README 栅格化成一张长图** | 无法搜索文本、无法复制安装命令、移动端字小如蚁、Git 无法 diff | 视觉层（Hero/分割线/画廊）用 SVG/PNG/GIF，正文与命令必须保留为原生 Markdown |
| **BL-2** | **禁止在提交的 `README.md` 中写入原始 ANSI 转义颜色码或 `<style>` 标签** | GitHub 会原样吐出乱码或直接剥离 `<style>` | 用 `shields.io` 徽章、Mermaid `classDef`、`<picture>` 亮暗图或 ASCII 灰度字符 `█▓▒░` 提供色彩与层次 |
| **BL-3** | **禁止捏造未验证的 Star 数、CI 绿标、覆盖率或虚假用户背书** | 违背 `github-readme` 与 `readme-rubric-audit` 诚信红线，一眼假 | 只挂反映仓库真实状态的徽章与实测数据（如真实评测分、真实文件数） |
| **BL-4** | **禁止在 `<details><summary>...` 后紧贴写 Markdown 而不留空行** | 缺少空行会导致 GFM 解析器把内部表格/代码块当成纯文本压扁 | `</summary>` 下方必须强制空一行再写 Markdown 内容 |
| **BL-5** | **禁止在 GitHub README 中使用带 Copy 按钮的 ASCII `█▓▒░` 代码块分割条并与 `## H2` 标题重复** | GitHub 会给代码块加灰色外框与复制图标，且半宽字符条加重复 H2 标题显得廉价冗余 | 一律生成 1200×56 矢量 SVG 章节头（`assets/readme/sec-01-*.svg`）配合 `<div id="..."></div>` 锚点 |
