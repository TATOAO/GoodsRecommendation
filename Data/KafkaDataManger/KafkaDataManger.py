import json
from typing import List

from kafka import KafkaConsumer

from Data.DataManager import DataManager


class KafkaDataManager(DataManager):
    def __init__(
        self,
        topics: List[str] = [],
        bootstrap_servers: str = "localhost:1234",
        topic: str = "xxxx",
        group_id: str = "xxxx",
    ):
        self.kafka_consumer = KafkaConsumer(
            topics,
            bootstrap_servers=bootstrap_servers,
            topic=topic,
            group_id=group_id,
            value_deserializer=self.value_deserliser,
        )

    def value_deserliser(self, message):
        message = json.loads(message.decode("utf-8"))

        # how to manipulate from kafka format to
        # the data implentation format

        return {key: value for key, value in message.items()}
