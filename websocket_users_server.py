import asyncio

import websockets
from websockets import ServerConnection

async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"{index} Сообщение получателя: {message}"
        await websocket.send(response)