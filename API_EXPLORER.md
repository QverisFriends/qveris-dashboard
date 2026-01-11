# Qveris API 探索器 - 新功能说明

## 🎯 新增功能：Qveris API 探索器

这是一个强大的工具搜索和测试平台，让用户可以探索 Qveris 平台上可用的所有工具。

## ✨ 功能亮点

### 1. 实时搜索
- 输入关键词（如 "weather"、"stock"、"AI"）
- 即时搜索 Qveris 平台上的 100+ 工具
- 显示匹配的工具列表

### 2. 工具详情展示
每个搜索结果显示：
- ✅ **工具名称** - 清晰的工具标识
- 📝 **描述** - 详细的功能说明
- 🏢 **提供商** - API 服务商名称
- ⏱️ **执行时间** - 平均响应时间（毫秒）
- ✅ **成功率** - 工具的稳定性能指标

### 3. 一键测试
点击"测试"按钮即可：
- 使用工具的示例参数
- 调用真实的 Qveris API
- 在模态框中展示完整返回数据

### 4. 结果展示
- JSON 格式化显示
- 语法高亮
- 清晰的成功/失败状态
- 支持复制查看

## 🔍 推荐搜索关键词

| 类别 | 关键词 | 示例 |
|------|---------|------|
| 天气 | weather, forecast, climate | "weather forecast" |
| 金融 | stock, price, trading | "stock price" |
| AI | chat, AI, model | "AI chat" |
| 地图 | map, location, route | "map location" |
| 社交 | social, media, weibo | "social media" |
| 学术 | paper, research, academic | "academic paper" |
| 电商 | product, shop, taobao | "ecommerce API" |
| 体育 | sports, game, race | "sports data" |

## 💡 使用技巧

1. **精确搜索** - 使用英文关键词效果更好
2. **查看统计** - 关注执行时间和成功率选择工具
3. **测试参数** - 查看示例参数了解如何使用
4. **批量测试** - 可以连续测试多个工具
5. **保存结果** - 好用的工具 ID 可以保存复用

## 🎨 UI/UX 亮点

- **流畅动画** - 搜索和结果加载都有丝滑过渡
- **悬停效果** - 鼠标悬停时卡片移动
- **模态框展示** - 结果在遮罩层中清晰展示
- **一键关闭** - 点击模态框外部或关闭按钮关闭
- **响应式** - 完美适配移动设备

## 📊 技术实现

```javascript
// 搜索工具
async function searchQverisTools() {
    const response = await fetch('https://qveris.ai/api/v1/tools/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + API_KEY
        },
        body: JSON.stringify({
            query: query,
            limit: 10
        })
    });
    // 展示搜索结果...
}

// 调用工具
async function testTool(toolId, sampleParams) {
    const response = await fetch(`https://qveris.ai/api/v1/tools/execute?tool_id=${toolId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + API_KEY
        },
        body: JSON.stringify({
            parameters: sampleParams,
            max_response_size: 20480
        })
    });
    // 展示调用结果...
}
```

## 🚀 快速体验

```bash
cd qveris-dashboard
python server.py

# 在浏览器中打开后：
# 1. 配置 API 密钥
# 2. 在"Qveris API 探索器"中输入 "weather"
# 3. 点击"测试"按钮查看结果
```

## 📱 移动端优化

- **全宽输入框** - 移动设备上输入更方便
- **触摸优化** - 按钮大小适合手指点击
- **模态框适配** - 移动端内边距自动调整
- **滚动优化** - 长列表和结果支持流畅滚动

---

**开始探索 Qveris 平台的无限可能！** ✨
