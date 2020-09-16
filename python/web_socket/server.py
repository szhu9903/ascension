import asyncio
import websockets

async def hello(websocket, path):
    async for message in websocket:
        greeting = "hello %s"%message
        await websocket.send(greeting)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(websockets.serve(hello,'localhost',8765))
    asyncio.get_event_loop().run_forever()
