
import pika
import json
# 创建连接
credentials = pika.PlainCredentials(username='zhu', password='zhu')
parameters = pika.ConnectionParameters(host='47.102.40.50',
                          port=5672,
                          virtual_host='/',
                          credentials=credentials)
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()

channel.queue_declare(queue='test')

channel.basic_publish(exchange='',
                      routing_key='test',
                      body= json.dumps({'name':'朱帅杰','phone':'15994092160'}))

print('success')
connection.close()

