#!/bin/bash
echo "🛠️  修复天气功能..."

# 1. 重启服务器
echo "1. 重启服务器..."
pkill -f "python.*server.py" 2>/dev/null
sleep 2
python server.py &
sleep 2

# 2. 测试API
echo "2. 测试天气API..."
python3 << 'PYEOF'
import requests
API_KEY = 'sk-VeJWtelcfNcqgm6H-V_TfkWX4Or2IyskjXqBvBszQ-k'
r = requests.post('https://qveris.ai/api/v1/tools/execute?tool_id=weather_api.current.retrieve.v1.dca6c0f0',
    json={'search_id': '', 'session_id': '', 'parameters': {'q': 'Beijing', 'aqi': 'yes'}, 'max_response_size': 20480},
    headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'})
d = r.json()
if d.get('success') and d.get('result', {}).get('data'):
    c = d['result']['data']['current']
    print(f"   ✅ 天气API正常: {c['temp_c']}°C, {c['condition']['text']}")
else:
    print(f"   ❌ 天气API失败")
PYEOF

echo ""
echo "✅ 修复完成!"
echo "🌐 请访问 http://localhost:9000"
echo "💡 提示: 按 Ctrl+F5 强制刷新浏览器"
