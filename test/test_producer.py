import asyncio
import websockets
import json
import time

async def send_events():
    uri = "ws://localhost:6789"  # URL do WebSocket do Producer
    async with websockets.connect(uri) as websocket:
        while True:
            # Cria um evento fictício
            event = {
                "event": "UserAction",
                "timestamp": time.time(),
                "details": {
                    "user_id": "123",
                    "action": "clicked_button",
                    "button_id": "btn-456"
                }
            }

            # Envia o evento para o WebSocket
            await websocket.send(json.dumps(event))
            print(f"Sent: {event}")

            # Aguardar antes de enviar o próximo evento
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(send_events())
