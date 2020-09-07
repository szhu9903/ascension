
import json,pika

credentials = pika.PlainCredentials(username='zhu',password='zhu')
parameters = pika.ConnectionParameters(host='47.102.40.50',
                          port=5672,
                          virtual_host='/',
                          credentials=credentials)
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()

channel.queue_declare(queue='test')

def get_queue(ch, method, properties, body):
    print(json.loads(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='test',
                      auto_ack=False,
                      on_message_callback=get_queue)
channel.start_consuming()