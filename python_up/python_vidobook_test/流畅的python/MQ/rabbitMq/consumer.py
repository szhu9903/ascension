
import pika
import json

credentials = pika.PlainCredentials(username='zhu',password='zhu')
parameters = pika.ConnectionParameters(host='47.102.40.50',
                                port=5672,
                                virtual_host='/',
                                credentials=credentials)
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()

channel.queue_declare(queue='test')

def get_queue(ch, method, properties, body):
    print('get %s'%json.loads(body))

channel.basic_consume(queue='test',
                      auto_ack=True,
                      on_message_callback=get_queue)

print('consumer queue')
channel.start_consuming()
