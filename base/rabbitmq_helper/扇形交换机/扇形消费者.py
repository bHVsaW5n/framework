import pika
import time
exchange = 'fanout_test'
# 建立连接

class Fun:
    # 各类回调函数
    def test_fun(self, ch, method, properties, body):
        try:
            # a = 8/0
            print("第一个消费者用的哦", str(body, encoding = "utf8") )
            # time.sleep(15)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(e)
            print("第一个消费者有错了哟~~")

    def test_fun2(self, ch, method, properties, body):
        try:
            print("第二个消费者用的哦", str(body, encoding = "utf8") )
            # time.sleep(15)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(e)
            print("第二个消费者有错了哟")

class Consume:

    def __init__(self, host='172.16.77.254', port=5672, virtual_host='/', user='admin', password='123123', exchange=exchange):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, virtual_host=virtual_host,
                                                                       credentials=pika.PlainCredentials(user, password)))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=exchange, exchange_type="fanout")


    def start_consume(self, fun):
        queue_name = "fanout1"
        self.channel.queue_declare(queue_name)
        self.channel.queue_bind(queue_name, exchange)

        self.channel.basic_consume(queue_name, fun)
        self.channel.start_consuming()
    #
    # def callback(self, ch, method, properties, body, fun):
    #     try:
    #         print("这事原来有错的，看他初步处理，处理几个", body)
    #         fun()
    #         ch.basic_ack(delivery_tag=method.delivery_tag)
    #     except Exception as e:
    #         print("这事原来有错的有错了")
    #     # pass



if __name__ == '__main__':

    consume = Consume()
    consume.start_consume(Fun().test_fun)

