from .client import KafkaClient
from dataclasses import dataclass
from confluent_kafka import Consumer

@dataclass
class KafkaConsumerConfig:
    bootstrap_servers: str
    group_id: str
    auto_offset_reset: str
    topic: str

class KafkaConsumer(KafkaClient):
    def __init__(self, config: KafkaConsumerConfig, message_handler):
        super().__init__(config)
        self.consumer = None
        self.message_handler = message_handler

    def connect(self):
        self.consumer = Consumer({
            "bootstrap.servers": self.config.bootstrap_servers,
            "group.id": self.config.group_id,
            "auto.offset.reset": self.config.auto_offset_reset
        })
        self.consumer.subscribe([self.config.topic])

    def close(self):
        self.consumer.close()

    def consume(self):
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue

            self.message_handler(msg.value().decode('utf-8'))