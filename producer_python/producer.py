import sys
from kafka import KafkaConsumer, KafkaProducer, TopicPartition
client = ["127.0.0.1:9092"]
topic = 'kafkatest' 
try:
  producer = KafkaProducer(bootstrap_servers=client)
except:
  print("error")
line = sys.stdin.readline()
while line:

    producer.send(topic, line)
    print("Sending "+line)
    line = sys.stdin.readline() 
