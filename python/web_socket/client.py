import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            name = input('name:')
            await websocket.send(name)
            serve_data = await websocket.recv()
            print(serve_data)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(hello('ws://localhost:8765'))