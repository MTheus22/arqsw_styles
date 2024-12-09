# consumer/app.py

from kafka import KafkaConsumer
import json
import asyncio
from websockets import serve
from messaging.consumer.config import CONSUMER_CONFIG
from messaging.consumer.logger import logger

class KafkaEventConsumer:
    def __init__(self, topic: str):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=CONSUMER_CONFIG['bootstrap_servers'],
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            group_id=CONSUMER_CONFIG['group_id'],
            auto_offset_reset=CONSUMER_CONFIG['offset_reset'],
            enable_auto_commit=True
        )

    def consume_events(self):
        for message in self.consumer:
            logger.info(f"Consumed event: {message.value}")
            yield message.value


async def websocket_handler(websocket, path):
    kafka_consumer = KafkaEventConsumer("user_events")
    try:
        for event in kafka_consumer.consume_events():
            try:
                # Tenta enviar os eventos para o cliente conectado
                await websocket.send(json.dumps(event))
            except websockets.exceptions.ConnectionClosed:
                # Aguarda por um novo cliente
                logger.warning("WebSocket connection closed. Waiting for a new connection.")
                break
            await asyncio.sleep(1)  # Evita consumo excessivo de CPU
    except Exception as e:
        logger.error(f"Error in WebSocket handler: {e}")
    finally:
        # Não feche o WebSocket servidor, apenas finalize a comunicação com o cliente
        logger.info("Awaiting new WebSocket client...")



if __name__ == "__main__":
    logger.info("Starting WebSocket server...")
    start_server = serve(websocket_handler, "0.0.0.0", 6788)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
