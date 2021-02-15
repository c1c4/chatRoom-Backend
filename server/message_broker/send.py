import pika


def send_stock_message(msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='stock_msg')

    channel.basic_publish(exchange='',
                          routing_key='stock_msg',
                          body=msg)
    print(f" [x] Sent {msg}")
    connection.close()
