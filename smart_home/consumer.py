from config import KAFKA_SERVERS, KAFKA_TOPIC


class Consumer:
    def __init__(self, kafka_topic: str = KAFKA_TOPIC, kafka_servers: list[str] = KAFKA_SERVERS, **kafka_params):
        from kafka import KafkaConsumer
        self.cons = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_servers, **kafka_params)

    def __iter__(self):
        return self.cons
