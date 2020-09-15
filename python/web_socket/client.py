import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        async for message in websocket:
            print(message)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(hello())




