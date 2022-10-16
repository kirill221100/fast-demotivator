import pika


class Dem:
    def __init__(self):
        self.response = b''
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='dem')
        self.channel.basic_consume(queue='dem', on_message_callback=self.callback, auto_ack=True)

    def callback(self, ch, method, properties, body):
        self.response = body

    def call(self, body):
        self.channel.basic_publish(exchange='', routing_key='dem', body=body)
        while self.response == b'':
            self.connection.process_data_events()
        return self.response
