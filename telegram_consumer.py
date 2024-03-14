from lib.kafka.consumer import KafkaConsumer
from lib.kafka.consumer import KafkaConsumerConfig
import os
import sys
[sys.path.append(i) for i in ['.', '..']]

# alphabet_range = os.getenv('ALPHABET_RANGE').split('-')

def print_message(message):
    print(f"Received message: {message}")

# def process_by_alphabet(message):
#     for message in consumer:
#         token = message.value['token']
#         if alphabet_range[0]<= token[0]<= alphabet_range[1]:
#             # Process the token
#             print(f"Processing token: {token}")
if __name__ == "__main__":
    consumer_config = KafkaConsumerConfig(
        # bootstrap_servers= "localhost:9092", # internal
        bootstrap_servers= "localhost:9094", # external
        group_id= "mygroup",
        auto_offset_reset= "earliest",
        topic= "mytopic"
    )
    

    consumer = KafkaConsumer(consumer_config, print_message)
    consumer.connect()
    print(consumer.consume())
    consumer.close()