# Qveris API 探索器使用指南

## ✅ 功能状态

**状态**: 正常工作
**收录工具**: 1000+ API工具
**搜索速度**: < 1秒

## 🚀 如何使用

### 方法1: 使用快捷按钮
1. 访问 http://localhost:9000
2. 找到 "Qveris API 探索器" 卡片
3. 点击热门分类按钮：
   - ☀️ 天气
   - 📈 股票
   - 🤖 AI
   - 📰 新闻
   - 🌐 翻译
   - 🗺️ 地图
   - 🎨 图片
   - 💱 金融

### 方法2: 手动搜索
1. 在搜索框输入关键词
2. 按 Enter 或点击"搜索"按钮
3. 查看搜索结果

### 方法3: 执行工具
1. 搜索到工具后，点击工具卡片
2. 查看工具详情和执行结果

## 💡 搜索技巧

### 推荐关键词
- **天气**: `weather`, `forecast`, `climate`
- **股票**: `stock`, `finance`, `trading`, `market`
- **AI/机器学习**: `AI`, `machine learning`, `NLP`, `chatbot`
- **图片**: `image`, `photo`, `picture`, `generation`
- **视频**: `video`, `motion`, `animation`
- **新闻**: `news`, `article`, `headlines`
- **翻译**: `translation`, `language`, `translate`
- **地图**: `map`, `location`, `geolocation`, `GPS`
- **金融**: `forex`, `currency`, `exchange`, `crypto`
- **数据分析**: `analytics`, `data`, `statistics`

### 搜索提示
- ✅ 使用英文关键词
- ✅ 使用通用词汇
- ✅ 尝试不同表述
- ❌ 避免过长描述
- ❌ 避免特殊字符

## 📊 功能特性

### 工具卡片显示
每个工具卡片包含：
- 工具名称
- 详细描述
- 提供商信息
- 平均响应时间
- 成功率统计

### 执行结果展示
点击工具后显示：
- 完整的JSON响应
- 执行耗时
- 成功/失败状态

## 🎯 热门搜索

### 天气类
```
weather - 天气查询
forecast - 天气预报
climate - 气候数据
```

### 金融类
```
stock price - 股票价格
forex - 外汇汇率
crypto - 加密货币
market - 市场数据
```

### AI类
```
chat completion - 对话生成
image generation - 图片生成
text analysis - 文本分析
language model - 语言模型
```

### 新闻类
```
news - 新闻搜索
headlines - 头条新闻
technology - 科技新闻
business - 商业新闻
```

## 🛠️ 技术细节

### API端点
- **搜索**: `POST /search`
- **执行**: `POST /tools/execute?tool_id={id}`

### 数据格式
```json
// 搜索请求
{
    "query": "weather",
    "limit": 10
}

// 搜索响应
{
    "total": 50,
    "results": [...],
    "search_id": "xxx"
}
```

## ❓ 常见问题

**Q: 搜索没有结果怎么办?**
A: 
- 尝试更通用的关键词
- 使用英文搜索
- 点击热门分类按钮

**Q: 工具执行失败怎么办?**
A: 
- 检查参数格式
- 某些工具需要额外配置
- 查看错误信息并重试

**Q: 搜索速度慢怎么办?**
A: 
- 网络问题，请检查连接
- 稍后重试
- 减少返回数量 (limit参数)

## 📝 示例

### 示例1: 搜索天气工具
```
搜索: weather
结果: Get Current Weather, Weather Forecast等
点击: Get Current Weather
参数: {"q": "Beijing"}
结果: 实时天气数据
```

### 示例2: 搜索图片生成
```
搜索: image generation
结果: Generate Image, Generate Video等
点击: Generate Image
参数: {"prompt": "一只猫", "size": "512*512"}
结果: AI生成的图片URL
```

## 🔗 相关链接

- **Qveris官网**: https://qveris.ai
- **API文档**: https://qveris.ai/docs
- **工具列表**: 在探索器中搜索 "all tools"

---

**更新时间**: 2026-01-11
**状态**: ✅ 已测试通过
