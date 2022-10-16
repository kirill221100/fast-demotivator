import pika, json
from dem import create_dem


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='dem')


def callback(ch, method, properties, body):
    body = json.loads(body)
    dem = create_dem(body['top_text'], body['bottom_text'], body['pic'])
    ch.basic_publish(exchange='', routing_key='dem', body=dem)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='dem', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
