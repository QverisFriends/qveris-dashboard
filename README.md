# Qveris 智能生活仪表盘

一个极具吸引力的现代化仪表盘应用，整合多个Qveris平台的高质量API，展示其实时交互能力。

## ✨ 核心功能

### 🌤️ 实时天气预报
- 显示当前温度、湿度、风速
- 空气质量指数（AQI）
- 动态天气图标和描述
- 一键刷新数据

### 📈 股票行情图表
- NVIDIA (NVDA) 实时股价
- 交互式折线图
- 涨跌幅显示（绿色上涨，红色下跌）
- 自动缩放和悬停提示

### 🤖 AI 智能助手
- 基于 Groq Llama 4 模型
- 实时对话交互
- 流畅的聊天界面
- 消息动画效果

### 📰 实时新闻资讯
- 使用 NewsData API 获取真实新闻
- 支持多语言新闻源
- 显示发布时间和来源
- 可点击跳转到原文

### 💱 实时汇率转换
- 支持 USD、EUR、CNY、JPY、GBP、AUD、CAD 等多种货币
- 实时汇率查询
- 快速转换计算
- 显示汇率详情

### 🗺️ 位置查询
- 基于 IP 地址定位
- 显示国家、省份、城市
- 显示运营商信息
- 显示经纬度坐标

### 🎨 AI 图片生成
- 使用智谱AI CogView-3 模型
- 支持自定义提示词
- 多种尺寸选择（1024x1024, 768x768, 512x512）
- 快速生成高质量图片

### 🎵 AI 语音合成
- 使用智谱AI GLM-TTS 模型
- 多种语音类型可选（童童、晓颜、晓松）
- 支持文本转语音
- 音频在线播放

### ₿ 加密货币新闻
- CryptoPanic 实时新闻
- 热门加密货币动态（BTC, ETH, SOL）
- 情绪分析显示（积极/消极）
- 多语言支持

### 👨‍💻 技术前沿
- Hacker News 热门故事
- 追踪最新技术趋势
- 显示分数和发布时间
- 快速跳转原文

### 📊 高级股票分析
- 多周期K线数据（5分钟/15分钟/30分钟/1小时）
- Financial Modeling Prep 数据源
- 交互式股票图表
- 支持任意股票代码查询

### 🎬 AI 视频生成
- 智谱AI Vidu Q1 模型
- 通用/动画两种风格
- 5秒1080P高质量视频
- 文本描述生成视频

### 📈 市场新闻与情感分析
- 基于 Alpha Vantage API
- 实时市场新闻
- 情感分析（积极/中性/消极）
- 主题分类展示

### 🔍 Qveris API 探索器
- 实时搜索 Qveris 平台工具
- 显示工具详情（名称、描述、提供商）
- 显示执行成功率和平均响应时间
- 一键测试 API 调用
- 模态框展示调用结果

### ⏰ 实时时钟
- 当前时间显示（秒级更新）
- 日期显示（中文格式）
- 渐变色文字效果

## 🎨 设计特色

- **玻璃拟态设计** - 现代化半透明卡片
- **渐变色主题** - 深色背景配紫蓝渐变
- **响应式布局** - 适配桌面和移动设备
- **平滑动画** - 所有交互都有流畅过渡
- **图标系统** - FontAwesome 精美图标
- **悬停效果** - 卡片悬停时的3D提升效果

## 🚀 快速开始

### 1. 获取 API 密钥

访问 [Qveris.ai](https://qveris.ai) 注册并获取你的API密钥。

### 2. 配置密钥

API密钥已预配置在 `index.html` 中。如需更换，修改第798行：

```javascript
const API_KEY = 'your_actual_api_key_here';
```

### 3. 运行应用

**方式一：直接打开**
```bash
# 在浏览器中直接打开 index.html
open index.html
```

**方式二：使用本地服务器**
```bash
# Python 3
python -m http.server 8000

# 或使用 Node.js
npx serve
```

然后访问 http://localhost:8000

## 📦 技术栈

- **HTML5** - 语义化结构
- **CSS3** - 动画和样式
- **JavaScript (ES6+)** - 逻辑和API调用
- **Chart.js** - 数据可视化
- **FontAwesome** - 图标库
- **Qveris API** - 统一的工具搜索和调用接口

## 🔧 使用的 Qveris API

| 功能 | API 提供商 | 工具 ID |
|------|-------------|----------|
| 天气预报 | WeatherAPI | weather_api.forecast.retrieve.v1.08e75758 |
| 股票数据 | Financial Modeling Prep | financialmodelingprep.historical_chart.1hour.retrieve.v1.8dda9f38 |
| AI 对话 | Groq | groq.groqapi.chat.completions.create.v1.19d0750a |
| 新闻资讯 | NewsData | newsdata.news.search.v1.b65ccc56 |
| 汇率转换 | Frankfurter | frankfurter.exchange_rates.retrieve_latest.v1 |
| 位置查询 | 百度地图 | baidu_map.ip_location.retrieve.v1 |
| AI 图片生成 | 智谱AI | bigmodel.images.generation.create.v1 |
| AI 语音合成 | 智谱AI | bigmodel.audio.speech.create.v4.4bb43cf8 |
| 加密货币新闻 | CryptoPanic | cryptopanic.api.posts.list.v2.db871245 |
| 技术新闻 | Hacker News | hackernews.top_stories_get.v1 |
| 多周期K线 | Financial Modeling Prep | financialmodelingprep.historical_chart.*.retrieve.v1.* |
| AI 视频生成 | 智谱AI | bigmodel.viduq1.videos.generations.create.v1.e6ac4b25 |
| 市场新闻 | Alpha Vantage | alphavantage.news_sentiment.query.v1.7aca3c4a |
| 工具搜索 | Qveris | tools/search |
| 工具执行 | Qveris | tools/execute |

## 🌟 亮点特性

1. **全面 API 集成** - 整合 Qveris 平台 15+ 种不同类别的 API
2. **实时数据更新** - 所有数据支持一键刷新，新闻实时获取
3. **API 探索器** - 搜索并测试 100+ Qveris 工具
4. **交互式图表** - Chart.js 提供平滑的股票图表
5. **美观界面** - 玻璃拟态 + 渐变色 + 动画
6. **响应式设计** - 完美适配各种屏幕尺寸
7. **无框架依赖** - 纯 HTML/CSS/JS 实现
8. **工具性能展示** - 显示执行时间和成功率统计
9. **AI 多模态能力** - 图片、语音、视频生成一体化

## 📱 响应式断点

- **桌面** - 多列网格布局，完整展示所有功能
- **平板** - 双列布局，优化触摸体验
- **移动** - 单列布局，简化操作流程

## 🔒 安全说明

- API密钥已预配置，请勿将代码分享时暴露密钥
- 建议在生产环境使用后端代理
- 本 Demo 仅用于演示，请根据需求调整
- API 探索器会调用真实的 Qveris 工具，请注意 API 配额限制

## 🔧 API 探索器使用技巧

1. **搜索关键词** - 输入 "weather"、"stock"、"AI"、"map" 等关键词
2. **查看详情** - 每个工具都显示提供商、执行时间、成功率
3. **测试调用** - 点击"测试"按钮使用示例参数调用 API
4. **查看结果** - 调用结果会在模态框中完整展示
5. **热门搜索示例**：
   - "weather forecast" - 天气相关工具
   - "stock price" - 股票和金融工具
   - "AI chat" - AI 和聊天机器人
   - "map location" - 地图和地理位置服务
   - "social media" - 社交媒体数据
   - "academic paper" - 学术论文搜索
   - "voice synthesis" - 语音合成工具
   - "video generation" - 视频生成工具

## 🎯 新增功能说明

### 🎵 AI 语音合成
- 使用智谱AI先进的TTS模型
- 支持多种中文语音
- 一键生成并在线播放

### ₿ 加密货币新闻
- 追踪BTC、ETH、SOL等主流币种
- 实时获取行业新闻
- 显示社区情绪倾向

### 👨‍💻 技术前沿
- 聚合Hacker News热门内容
- 掌握最新技术动态
- 便捷的原文跳转

### 📊 高级股票分析
- 多时间周期K线图
- 支持任意美股查询
- 专业级图表展示

### 🎬 AI 视频生成
- 5秒高质量AI视频
- 通用/动画双风格
- 文本描述转视频

## 📄 许可证

MIT License - 自由使用、修改和分发

## 🙏 致谢

感谢 Qveris 平台及其合作伙伴提供的高质量 API 服务：
- **WeatherAPI** - 全球天气数据
- **Financial Modeling Prep** - 股票和金融数据
- **Groq** - 快速 AI 推理
- **NewsData** - 实时新闻资讯
- **Frankfurter** - 汇率数据
- **百度地图** - 位置服务
- **智谱AI** - AI 图片/语音/视频生成
- **CryptoPanic** - 加密货币新闻
- **Hacker News** - 技术新闻
- **Alpha Vantage** - 市场新闻与情感分析
- **Qveris 平台** - 统一的工具搜索和调用接口

---

**立即体验 Qveris 平台的强大能力！** 🚀
