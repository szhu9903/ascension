import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8759') as websocket:
        name = input('name:')
        await websocket.send(name)
        print(name)
        greeting = await websocket.recv()
        print(greeting)

asyncio.get_event_loop().run_until_complete(hello())
