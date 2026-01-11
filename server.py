#!/usr/bin/env python3
"""
Qveris 智能生活仪表盘 - 本地服务器
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 9000
DIRECTORY = "."


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


def run_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("\n" + "=" * 50)
    print("  🚀 Qveris 智能生活仪表盘")
    print("=" * 50)
    print(f"\n✅ 服务器启动成功！")
    print(f"📍 访问地址: http://localhost:{PORT}")
    print(f"📁 工作目录: {os.getcwd()}")
    print(f"\n💡 提示:")
    print(f"   1. 在 index.html 中配置你的 Qveris API 密钥")
    print(f"   2. 按 Ctrl+C 停止服务器")
    print("\n" + "=" * 50 + "\n")

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 服务器已停止")


if __name__ == "__main__":
    run_server()
