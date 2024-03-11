from .client import KafkaClient
from confluent_kafka import Producer
from dataclasses import dataclass

@dataclass
class KafkaProducerConfig:
    bootstrap_servers: str

class KafkaProducer(KafkaClient):
    def __init__(self, config):
        super().__init__(config)
        self.producer = None

    def connect(self):
        self.producer = Producer({
            "bootstrap.servers": self.config.bootstrap_servers,                          
        })

    def close(self):
        self.producer.flush()

    def produce(self, topic, message):
        self.producer.produce(topic, message, callback=self.delivery_report)
        self.producer.flush()

    def delivery_report(self, err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    
# for data in some_data_source:
#     # Trigger any available delivery report callbacks from previous produce() calls
#     p.poll(0)

#     # Asynchronously produce a message. The delivery report callback will
#     # be triggered from the call to poll() above, or flush() below, when the
#     # message has been successfully delivered or failed permanently.
#     p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
# p.flush()