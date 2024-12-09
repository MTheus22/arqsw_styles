# test/test_producer.py

from kafka import KafkaProducer
import json
import asyncio
import websockets
from messaging.producer.config import PRODUCER_CONFIG
from messaging.producer.logger import logger


class KafkaEventProducer:
    def __init__(self, topic: str):
        self.producer = KafkaProducer(
            bootstrap_servers=PRODUCER_CONFIG['bootstrap_servers'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            retries=PRODUCER_CONFIG['retries']
        )
        self.topic = topic

    def send_event(self, event: dict):
        """
        Envia um evento ao Kafka.
        """
        try:
            future = self.producer.send(self.topic, event)
            result = future.get(timeout=10)  # Aguarda a confirmação do envio
            logger.info(f"Event sent successfully to {self.topic}: {event}")
        except Exception as e:
            logger.error(f"Failed to send event to {self.topic}: {e}")
            raise

    def close(self):
        """
        Fecha o Producer de forma segura.
        """
        self.producer.close()


async def websocket_handler(websocket, path):
    """
    Manipula mensagens recebidas via WebSocket e envia para o Kafka.
    """
    producer = KafkaEventProducer(PRODUCER_CONFIG['topic'])
    try:
        async for message in websocket:
            logger.info(f"Received message from WebSocket: {message}")
            event = json.loads(message)  # Converte a mensagem recebida para JSON
            producer.send_event(event)  # Envia o evento ao Kafka
    except Exception as e:
        logger.error(f"Error in WebSocket handler: {e}")
    finally:
        producer.close()


if __name__ == "__main__":
    topic_name = PRODUCER_CONFIG['topic']
    logger.info(f"Starting WebSocket producer server on topic {topic_name}...")

    # Inicia o servidor WebSocket
    start_server = websockets.serve(websocket_handler, "0.0.0.0", 6789)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
