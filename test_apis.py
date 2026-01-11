#!/usr/bin/env python3
"""
Qveris Dashboard API 测试脚本
验证所有集成的API功能是否正常工作
"""

import asyncio
import aiohttp
import json
from datetime import datetime

# 配置
API_KEY = "sk-VeJWtelcfNcqgm6H-V_TfkWX4Or2IyskjXqBvBszQ-k"
BASE_URL = "https://qveris.ai/api/v1"

HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# 测试用例
TESTS = [
    {
        "name": "天气预报",
        "tool_id": "weather_api.forecast.retrieve.v1.08e75758",
        "parameters": {"q": "Beijing", "days": 3, "aqi": "yes"},
    },
    {
        "name": "股票数据",
        "tool_id": "financialmodelingprep.historical_chart.1hour.retrieve.v1.8dda9f38",
        "parameters": {"symbol": "NVDA"},
    },
    {
        "name": "AI对话",
        "tool_id": "groq.groqapi.chat.completions.create.v1.19d0750a",
        "parameters": {
            "model": "meta-llama/llama-4-maverick-17b-128e-instruct",
            "messages": [{"role": "user", "content": "你好"}],
            "max_tokens": 100,
        },
    },
    {
        "name": "新闻搜索",
        "tool_id": "newsdata.news.search.v1.b65ccc56",
        "parameters": {"q": "technology", "language": "en", "size": 5},
    },
    {
        "name": "汇率查询",
        "tool_id": "frankfurter.exchange_rates.retrieve_latest.v1",
        "parameters": {"from": "USD", "to": "CNY"},
    },
    {
        "name": "IP定位",
        "tool_id": "baidu_map.ip_location.retrieve.v1",
        "parameters": {},
    },
    {
        "name": "AI图片生成",
        "tool_id": "bigmodel.images.generation.create.v1",
        "parameters": {"model": "cogview-3", "prompt": "一只猫", "size": "512*512"},
    },
    {
        "name": "AI语音合成",
        "tool_id": "bigmodel.audio.speech.create.v4.4bb43cf8",
        "parameters": {"input": "你好", "model": "glm-tts", "voice": "tongtong"},
    },
    {
        "name": "加密货币新闻",
        "tool_id": "cryptopanic.api.posts.list.v2.db871245",
        "parameters": {"api_plan": "growth", "currencies": "BTC,ETH", "size": 5},
    },
    {
        "name": "Hacker News",
        "tool_id": "hackernews.top_stories_get.v1",
        "parameters": {},
    },
    {
        "name": "15分钟K线",
        "tool_id": "financialmodelingprep.historical_chart.15min.retrieve.v1.f95a7510",
        "parameters": {"symbol": "AAPL"},
    },
    {
        "name": "市场新闻",
        "tool_id": "alphavantage.news_sentiment.query.v1.7aca3c4a",
        "parameters": {
            "function": "NEWS_SENTIMENT",
            "topics": "technology",
            "limit": 5,
        },
    },
]


async def test_api(session, test):
    """测试单个API"""
    url = f"{BASE_URL}/tools/execute?tool_id={test['tool_id']}"

    payload = {
        "search_id": "",
        "session_id": "",
        "parameters": test["parameters"],
        "max_response_size": 20480,
    }

    try:
        async with session.post(url, json=payload, headers=HEADERS) as response:
            data = await response.json()

            if data.get("success") and data.get("result"):
                return {
                    "name": test["name"],
                    "status": "✅ 成功",
                    "latency": f"{data.get('elapsed_time_ms', 0)}ms",
                    "data_size": len(str(data.get("result", {}))),
                }
            else:
                return {
                    "name": test["name"],
                    "status": "❌ 失败",
                    "error": data.get("error_message", "Unknown error"),
                }
    except Exception as e:
        return {"name": test["name"], "status": "❌ 异常", "error": str(e)}


async def run_tests():
    """运行所有测试"""
    print("\n" + "=" * 60)
    print("🧪 Qveris Dashboard API 测试")
    print("=" * 60)
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"API密钥: {API_KEY[:20]}...")
    print("=" * 60 + "\n")

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[test_api(session, test) for test in TESTS])

    # 显示结果
    success_count = 0
    for i, result in enumerate(results, 1):
        status_icon = "✅" if "成功" in result["status"] else "❌"
        print(f"{i:2d}. {result['name']:<15} {status_icon} {result['status']}")

        if "latency" in result:
            print(f"    └─ 延迟: {result['latency']}")
        elif "error" in result:
            print(f"    └─ 错误: {result['error'][:50]}")

        if "成功" in result["status"]:
            success_count += 1

    print("\n" + "=" * 60)
    print(f"📊 测试结果: {success_count}/{len(TESTS)} 通过")
    print("=" * 60 + "\n")

    return success_count


async def test_search():
    """测试工具搜索功能"""
    print("🔍 测试工具搜索功能...\n")

    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{BASE_URL}/search",
            json={"query": "AI image generation", "limit": 5},
            headers=HEADERS,
        ) as response:
            data = await response.json()

            if data.get("results"):
                print(f"找到 {len(data['results'])} 个相关工具:\n")
                for i, tool in enumerate(data["results"][:3], 1):
                    print(f"{i}. {tool['name']}")
                    print(f"   └─ {tool['description'][:80]}...")
                    print(f"   └─ 提供商: {tool['provider_description'].split('.')[0]}")
                    print()
            else:
                print("未找到相关工具\n")


async def main():
    """主函数"""
    await test_search()
    await run_tests()

    print("📝 测试完成!")
    print("\n💡 提示:")
    print("   - 打开 http://localhost:9000 查看完整仪表盘")
    print("   - 所有API已集成到index.html中")
    print("   - 使用API探索器搜索更多工具\n")


if __name__ == "__main__":
    asyncio.run(main())
