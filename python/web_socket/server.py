
import websockets
import asyncio


async def hello(websocket, path):
    print('hello')
    name = await websocket.recv()
    print(name)
    greeting = 'hello %s'%name
    await websocket.send(greeting)
    print(greeting)

start_server = websockets.serve(hello,'localhost',8759)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


