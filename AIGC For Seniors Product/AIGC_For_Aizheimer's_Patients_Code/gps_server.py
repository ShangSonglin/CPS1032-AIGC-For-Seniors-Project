import asyncio
import websockets

async def gps_server(websocket, path):
    print("客户端已连接")
    try:
        async for message in websocket:
            gps_data = message  # 接收 HTML 页面发送的数据
            print(f"接收到的 GPS 数据: {gps_data}")
    except websockets.exceptions.ConnectionClosed:
        print("客户端已断开连接")

# 启动 WebSocket 服务器
start_server = websockets.serve(gps_server, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()