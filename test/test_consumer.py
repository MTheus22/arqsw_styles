# test/test_consumer.py

import asyncio
import websockets

async def test_websocket():
    uri = "ws://localhost:8000/consume-events"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}")

asyncio.run(test_websocket())
