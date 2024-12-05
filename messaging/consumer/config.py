# consumer/config.py

CONSUMER_CONFIG = {
    "bootstrap_servers": ["compose-kafka-1:9092"],
    "group_id": "user_event_consumers",
    "offset_reset": "latest",
}
