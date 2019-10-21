from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import randint,uniform
import json,time

time.sleep(50)
producer = KafkaProducer(bootstrap_servers=['kafka_cluster:9092']
                         , value_serializer=lambda m: json.dumps(m).encode('ascii')
                )

for n in range(1,2000):
    match = randint(100,999)
    price = "{0:.2f}".format(uniform(1,10))
    producer.send('prices-topic', {match: price})

print("Messages sent")