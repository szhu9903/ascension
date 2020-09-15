import asyncio
import websockets

async def server(websocket, path):
    while True:
        message = input('name:')
        await websocket.send(message)


if __name__ == '__main__':
    start_server = websockets.serve(server, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


