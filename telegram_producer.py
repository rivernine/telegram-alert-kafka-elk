from lib.kafka.producer import KafkaProducer
from lib.kafka.producer import KafkaProducerConfig

if __name__ == "__main__":
    producer_config = KafkaProducerConfig(
        bootstrap_servers = 'localhost:9094'
    ) 

    producer = KafkaProducer(producer_config)
    producer.connect()
    producer.produce('mytopic', 'Hello, World!')
    producer.close()