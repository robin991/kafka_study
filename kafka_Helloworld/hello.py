'''
Basic hello function to showcase the funcitoning of Kafka

https://www.youtube.com/watch?v=w6A-uDEb7JY&list=PLjfRmoYoxpNrs0VmIq6mOTqXP52RfZdRf
'''


from time import sleep
from json import dumps 
from kafka import KafkaProducer 
topic_name = "hello_world"

producer = KafkaProducer(bootstrap_servers = ['localhost:9092'],
                         value_serializer = lambda x: dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number' : e}
    print(data)
    producer.send(topic_name, value = data)
    sleep(5)
