#!/bin/bash
# 快速启动Qveris仪表盘

echo "🚀 启动 Qveris 智能生活仪表盘..."

# 终止占用9000端口的进程
fuser -k 9000/tcp 2>/dev/null
sleep 1

# 启动服务器
python server.py &
sleep 2

# 测试
if curl -s http://localhost:9000 > /dev/null; then
    echo "✅ 启动成功!"
    echo "🌐 访问: http://localhost:9000"
else
    echo "❌ 启动失败"
fi
