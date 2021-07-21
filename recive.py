import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

print('[*] We are waiting for you, Neo')

def callback(ch, method, properties, body):
    print(" [X] folow the damn' rabbit!  %r" %body)

channel.basic_consume(queue='hello', auto_ack=True, on_message_callback = callback)

channel.start_consuming()
