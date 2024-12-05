# messaging/producer/config.py

PRODUCER_CONFIG = {
    "bootstrap_servers": ["compose-kafka-1:9092"],
    "retries": 5,
    "topic": "user_events"
}
