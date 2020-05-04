# import pika
# import time
# queue_name = "hello"
# # 建立连接
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.77.254', port=5672, virtual_host="/",
#                                                                credentials=pika.PlainCredentials("admin", "123123")))
# channel = connection.channel()
# channel.queue_declare(queue=queue_name)
#
# def callback(ch, method, properties, body):
#     try:
#         print(body)
#     except Exception as e:
#         print("有错了")
#     # pass
#
#
# channel.basic_consume(queue_name, callback, auto_ack=False)
# channel.start_consuming()
from base.rabbitmq_helper.consumer import Consume, Fun

if __name__ == '__main__':

    consume = Consume()
    consume.start_consume(Fun().test_fun2)