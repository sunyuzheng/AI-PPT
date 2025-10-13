# AI-PPT

## 简介
使用 Reveal.js 构建的《AI for Everyone》主题演示文稿，面向 Lead Forward · Bay Area WeChat Group。演示内容围绕 AI 范式转移、学习路径与课程资源展开。

## 本地预览
1. 安装任意静态服务器工具，例如 `serve`：
   ```bash
   npm install -g serve
   ```
2. 在仓库根目录运行：
   ```bash
   serve docs
   ```
3. 浏览器访问 `http://localhost:3000`（或终端提示的地址）。

也可以直接在文件管理器中双击 `docs/index.html` 进行离线浏览。

## 部署到 GitHub Pages
1. 将仓库推送到 GitHub。
2. 在仓库设置中启用 GitHub Pages，Source 选择 `work`（或主分支），目录选择 `/docs`。
3. 几分钟后即可通过 Pages 提供的 URL 分享幻灯片。

## 文件结构
```
AI-PPT/
├── docs/
│   ├── index.html   # Reveal.js 幻灯片
│   └── styles.css   # 自定义主题样式
└── README.md
```

## 其他说明
- 幻灯片使用 CDN 引用 Reveal.js，无需额外构建步骤。
- 如需导出 PDF，可在浏览器中打开演示后使用 `?print-pdf` 参数并通过打印对话框保存。
