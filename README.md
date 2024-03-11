# Kafka

# Prerequisites
||name|version|
|:-:|:-:|:-:|
|infra|docker|24.0.6|
|infra|docker-compose|1.29.2|
|lang|python|3.8|
|lib|kafka broker|docker.io/bitnami/kafka:3.6|
|lib|kafka client|confluent kafka|
|tool|broker |confluent kafka|

# Broker


# Client

# Cli
```sh
# kafka topic create
kafka-topics.sh --create --topic <topic_name> --partitions <num_of_partitions> --bootstrap-server localhost:9092

# kafka topic list
kafka-topics.sh --list --bootstrap-server localhost:9092
```
