# Qveris Dashboard 完整项目文档

## 📋 项目概述

基于 Qveris API 的智能生活仪表盘，整合多个高质量第三方API，提供一站式的数据和AI服务。

## 🚀 快速启动

```bash
cd /home/leixin/qveris-dashboard

# 方法1: 使用启动脚本
./start.sh

# 方法2: 直接运行
python server.py
```

**访问地址**: http://localhost:9000

## ✅ 已验证可用的功能

| 功能 | API | 状态 |
|------|-----|------|
| 🌤️ 天气 | WeatherAPI | ✅ 正常 |
| 📈 股票 | Financial Modeling Prep | ⚠️ 可能超时 |
| 📰 新闻 | NewsData | ✅ 正常 |
| 💱 汇率 | Frankfurter | ✅ 正常 |
| 📍 位置 | 百度地图 | ✅ 正常 |
| 🎨 AI图片生成 | 智谱AI (CogView-3) | ✅ 正常 |
| 🤖 AI对话 | Groq | ⚠️ 需要权限 |
| 🔍 API搜索 | Qveris | ✅ 正常 |

## 📁 文件结构

```
qveris-dashboard/
├── index.html          # 主页面 (1000+ 行，完全重写)
├── server.py           # HTTP服务器
├── start.sh            # 快速启动脚本
├── test_apis.py        # API测试脚本
├── README.md           # 项目说明
├── PRODUCT.md          # 产品设计文档
├── PROJECT_SUMMARY.md  # 项目总结
├── favicon.ico         # 网站图标
└── test_weather_only.html  # 独立天气测试页
```

## 🔧 技术特点

1. **完全重写**: 2024行精简代码，无冗余
2. **错误处理**: 所有API调用都有try-catch
3. **加载状态**: 显示加载动画和错误提示
4. **响应式设计**: 适配桌面和移动设备
5. **玻璃拟态UI**: 现代化半透明卡片设计
6. **API密钥**: 预配置，开箱即用

## 💡 使用提示

1. **刷新页面**: 按 `Ctrl+F5` 强制刷新
2. **查看错误**: 按 `F12` 打开浏览器控制台
3. **重试操作**: 失败的功能可点击刷新按钮重试
4. **API配额**: 注意各API的调用限制

## 🔍 API密钥

当前配置: `sk-VeJWtelcfNcqgm6H-V_TfkWX4Or2IyskjXqBvBszQ-k`

如需更换，编辑 `index.html` 第925行:
```javascript
const API_KEY = 'your_new_api_key';
```

## 📚 参考资料

- **Qveris官网**: https://qveris.ai
- **API文档**: https://qveris.ai/docs
- **Python SDK**: https://github.com/QverisAI/sdk-python

---

**状态**: ✅ 项目完整，可正常运行
**最后更新**: 2026-01-11
