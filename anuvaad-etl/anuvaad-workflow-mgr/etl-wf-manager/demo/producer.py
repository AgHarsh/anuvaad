import json
import logging
import traceback

import os
import datetime as dt
from kafka import KafkaProducer

log = logging.getLogger('file')
cluster_details = os.environ.get('KAFKA_CLUSTER_DETAILS', 'localhost:9092')
consumer_poll_interval = os.environ.get('CONSUMER_POLL_INTERVAL', 10)


class Producer:

    def __init__(self):
        pass

    # Method to instantiate producer
    # Any other method that needs a producer will get it from her
    def instantiate(self):
        producer = KafkaProducer(bootstrap_servers=[cluster_details],
                                 api_version=(1, 0, 0),
                                 value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        return producer

    # Method to push records to a topic in the kafka queue
    def push_to_queue(self, object_in, topic):
        producer = self.instantiate()
        print("Pushing to the Kafka Queue......")
        log.info("Pushing to the Kafka Queue......")
        try:
            log.info(object_in)
            producer.send(topic, value=object_in)
            producer.flush()
            log.info("Done.")
        except Exception as e:
            log.error("Exception while producing: " + str(e))
            traceback.print_exc()