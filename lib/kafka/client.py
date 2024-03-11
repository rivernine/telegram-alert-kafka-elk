from abc import ABC, abstractmethod

class KafkaClient(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass