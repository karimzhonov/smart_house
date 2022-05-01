from config import KAFKA_TOPIC, KAFKA_SERVERS


class Producer:
    def __init__(self, kafka_topic: str = KAFKA_TOPIC, kafka_servers: list[str] = KAFKA_SERVERS, **kafka_params):
        from kafka import KafkaProducer
        self.kafka_topic = kafka_topic
        self.prod = KafkaProducer(bootstrap_servers=kafka_servers, **kafka_params)

    def send(self, value = None, **kwargs):
        return self.prod.send(self.kafka_topic, value, **kwargs)

    def flush(self, timeout=None):
        return self.prod.flush(timeout)
