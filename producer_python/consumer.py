import sys
from kafka import KafkaConsumer, KafkaProducer, TopicPartition
client = ["127.0.0.1:9092"]
topic = 'kafkatest' 
try:
  tp = TopicPartition(topic,0)
  consumer = KafkaConsumer(bootstrap_servers=client)
  consumer.assign([tp])
  consumer.seek_to_beginning(tp)
  for message in consumer:
     print(message)
except Exception as e:
  print("error")
  print(e)
