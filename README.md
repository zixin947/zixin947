<div align="center">

# 你好，我是 Zixin 👋

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;size=21&amp;duration=3200&amp;pause=1000&amp;color=38BDF8&amp;center=true&amp;vCenter=true&amp;width=640&amp;lines=AI+Agents+%26+LLM+Tooling;Context+Engineering+%26+Agent+Runtime;Building+Tools+%C2%B7+Contributing+Upstream" width="640" alt="AI Agents 与 LLM 工具 · 上下文工程与 Agent Runtime · 工具开发与开源贡献" />

**AI Agent 与 LLM 开发者 · 上下文工程 · 开源贡献**

围绕 Agent Runtime、上下文压缩与模型集成，构建更实用的开发工具。<br>
把想法做成工具，也把修复带回上游。

<p>
  <a href="https://github.com/zixin947?tab=repositories"><img src="https://img.shields.io/badge/GitHub-zixin947-181717?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="浏览我的 GitHub 项目" /></a>
  <a href="https://github.com/zixin947/dsh-compact"><img src="https://img.shields.io/badge/Focus-Context_Engineering-0284C7?style=for-the-badge&amp;logo=buffer&amp;logoColor=white" alt="关注方向：上下文工程" /></a>
  <a href="https://github.com/zixin947/dsh-compact/issues"><img src="https://img.shields.io/badge/Let's_Talk-GitHub_Issues-0F766E?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="通过 GitHub Issues 交流" /></a>
</p>

[代表项目](#projects) · [开源贡献](#contributions) · [技术与工程](#stack) · [开发足迹](#activity)

</div>

---

## ⚡ 关于我

- **开发与贡献：** AI Agents、Context Engineering、Tool Use、模型 Provider 与 AI Tooling。
- **上下文工程：** 在 `dsh-compact` 中实现自动与手动压缩、工具结果裁剪和有界溢出恢复。
- **桌面工具：** 在 `Codex Atelier` 中探索 Tauri 2 + Vue 3 的开发工作台与环境管理交互。
- **学习与探索：** RAG、Agentic RAG、Agent Memory、MCP 与 LLM 应用评估。

---

<a id="projects"></a>

## 🚀 代表项目

<table>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🧩 <a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Our Free Model / OFM</a></h3>
      <p align="center"><b>连接模型渠道与开发工具</b><br>主要维护者</p>
      <p align="center">
        <a href="https://github.com/Ebony-Vinyl/dsh-our-free-model/stargazers"><img src="https://img.shields.io/github/stars/Ebony-Vinyl/dsh-our-free-model?style=flat-square&amp;color=38bdf8&amp;label=Upstream%20Stars" alt="OFM 上游 Stars" /></a>
        <img src="https://img.shields.io/badge/JavaScript-Plugin-F7DF1E?style=flat-square&amp;logo=javascript&amp;logoColor=black" alt="JavaScript 插件" />
        <a href="https://github.com/Ebony-Vinyl/dsh-our-free-model/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-34d399?style=flat-square" alt="MIT 许可证" /></a>
      </p>
      <ul>
        <li><b>模型接入：</b>为 DeepSeek Harness 整合多种模型渠道、账号与 Provider。</li>
        <li><b>本地网关：</b>提供 OpenAI 兼容接口，连接其它开发工具与客户端。</li>
        <li><b>使用体验：</b>包含模型管理、用量看板、运行日志与应用内升级。</li>
        <li><b>维护工作：</b>账号渠道的排队换号、请求级重试保护与相关修复。</li>
      </ul>
      <p align="center"><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model#readme"><b>查看项目 →</b></a> · <a href="https://github.com/Ebony-Vinyl/dsh-our-free-model/pulls?q=is%3Apr+is%3Amerged+author%3Azixin947"><b>我的贡献 →</b></a></p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🖥️ <a href="https://github.com/zixin947/codex-atelier">Codex Atelier</a></h3>
      <p align="center"><b>为开发工作流留一间工作室</b></p>
      <p align="center">
        <a href="https://github.com/zixin947/codex-atelier/stargazers"><img src="https://img.shields.io/github/stars/zixin947/codex-atelier?style=flat-square&amp;color=38bdf8" alt="Codex Atelier Stars" /></a>
        <img src="https://img.shields.io/badge/Tauri-2-24C8D8?style=flat-square&amp;logo=tauri&amp;logoColor=white" alt="Tauri 2" />
        <img src="https://img.shields.io/badge/Status-Prototype-FBBF24?style=flat-square" alt="当前为原型" />
      </p>
      <ul>
        <li><b>桌面原型：</b>使用 Tauri 2、Vue 3 与 TypeScript 构建独立伴侣工作站。</li>
        <li><b>工作台交互：</b>探索环境概览、扩展管理、诊断与回退的界面组织。</li>
        <li><b>视觉设计：</b>米灰机壳、下沉仪表屏与薄荷绿键帽，营造有触感的工作空间。</li>
        <li><b>当前进度：</b>行为插件管理已接入本机能力；主工作台等模块仍使用演示数据。</li>
      </ul>
      <p align="center"><a href="https://github.com/zixin947/codex-atelier#preview"><b>查看界面与功能进度 →</b></a></p>
    </td>
  </tr>
</table>

---

<a id="contributions"></a>

## 🌐 开源贡献

参与 DeepSeek Harness 生态的插件、桌面客户端与模型集成开发，通过修复、文档和回归验证向上游贡献。

| 上游项目 | 项目方向 | 我的贡献记录 |
| :--- | :--- | :--- |
| [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | 终端界面与 Agent 会话工具 | [查看已合并 PR](https://github.com/ccch1mneyyy/dsh-TUI/pulls?q=is%3Apr+is%3Amerged+author%3Azixin947) |
| [EAC Desktop](https://github.com/Ebony-Vinyl/EAC-Desktop) | DeepSeek Harness 插件整合与桌面客户端 | [查看已合并 PR](https://github.com/Ebony-Vinyl/EAC-Desktop/pulls?q=is%3Apr+is%3Amerged+author%3Azixin947) |
| [Our Free Model / OFM](https://github.com/Ebony-Vinyl/dsh-our-free-model) | 模型 Provider 与 LLM 工具 | [查看已合并 PR](https://github.com/Ebony-Vinyl/dsh-our-free-model/pulls?q=is%3Apr+is%3Amerged+author%3Azixin947) |

<p align="center">
  <a href="https://github.com/search?q=is%3Apr+is%3Apublic+is%3Amerged+author%3Azixin947+-user%3Azixin947&amp;type=pullrequests"><img src="https://img.shields.io/badge/Upstream-Merged_PRs-238636?style=for-the-badge&amp;logo=git-pull-request&amp;logoColor=white" alt="查看公开上游已合并 PR" /></a>
  <a href="https://github.com/search?q=is%3Apr+is%3Apublic+is%3Aopen+author%3Azixin947+-user%3Azixin947&amp;type=pullrequests"><img src="https://img.shields.io/badge/In_Progress-Open_PRs-0284C7?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="查看公开上游进行中的 PR" /></a>
</p>

---

<a id="stack"></a>

## 🛠️ 技术与工程

| 方向 | 技术与实践 |
| :--- | :--- |
| **AI / LLM** | DeepSeek Harness、Agent 插件、上下文压缩、模型 Provider、工具调用 |
| **应用与工具** | JavaScript、TypeScript、Node.js、HTTP / SSE、Vue 3、Electron |
| **全栈基础** | Java、Spring Boot、MySQL |
| **工程实践** | Git、GitHub Actions、回归测试、插件集成 |
| **正在探索** | RAG、Agent Memory、MCP、LLM 应用评估 |

<p align="center">
  <img src="https://skillicons.dev/icons?i=js,ts,nodejs,vue,java,spring,mysql,electron,tauri,git,github,githubactions&amp;perline=6" width="360" alt="JavaScript、TypeScript、Node.js、Vue、Java、Spring、MySQL、Electron、Tauri、Git、GitHub 与 GitHub Actions" />
</p>

---

<a id="activity"></a>

## 📊 开发足迹

<p align="center">
  <a href="https://github.com/search?q=is%3Apr+is%3Apublic+is%3Amerged+author%3Azixin947+-user%3Azixin947&amp;type=pullrequests"><img src="assets/github-stats.svg" width="49%" alt="GitHub 公开仓库、关注者与上游已合并 PR 统计" /></a>
  <a href="https://github.com/zixin947?tab=repositories"><img src="assets/github-languages.svg" width="49%" alt="dsh-compact 与 codex-atelier 两个个人项目的代码语言字节分布，不代表熟练度" /></a>
</p>

<p align="center"><sub>卡片每 6 小时更新一次；语言分布仅统计 dsh-compact 与 codex-atelier，按 GitHub 返回的代码字节数计算。</sub></p>

### 🐍 贡献轨迹

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/github-contribution-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/github-contribution-snake.svg" />
  <img src="assets/github-contribution-snake.svg" width="100%" alt="GitHub 贡献日历的贪吃蛇动画" />
</picture>

---

## 🤝 交流与协作

欢迎围绕 **Agent 工具、上下文工程、模型集成与桌面交互**交流想法。

- [dsh-compact Issues](https://github.com/zixin947/dsh-compact/issues)：插件使用、兼容性与问题反馈。
- [Codex Atelier Issues](https://github.com/zixin947/codex-atelier/issues)：界面建议、原型体验与功能讨论。

<div align="center">

**让工具更顺手，让想法走得更远。**

<a href="https://github.com/zixin947?tab=followers"><img src="https://img.shields.io/github/followers/zixin947?style=flat-square&amp;label=Followers&amp;color=38bdf8" alt="GitHub Followers" /></a>
<a href="https://github.com/zixin947/zixin947/blob/main/docs/profile-design.md"><img src="https://img.shields.io/badge/Profile-Markdown_%2B_SVG-34d399?style=flat-square" alt="主页设计与维护说明" /></a>

</div>
