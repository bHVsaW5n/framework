import pika

# 建立连接
exchange = 'fanout_test'


class Publish:
    """
    直连交换机
    """

    def __init__(self,  host='172.16.77.254', port=5672, virtual_host="/", admin='admin', password='123123',
                 exchange=exchange):
        self.exchange = exchange
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port, virtual_host=virtual_host,
                                      credentials=pika.PlainCredentials(admin, password)))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=exchange, exchange_type='fanout')
        self.exchange = exchange
        # self.queue = queue

    def start_publish(self, message):
        self.channel.basic_publish(exchange=self.exchange,routing_key='', body=message,
                                   properties=pika.BasicProperties(delivery_mode=2))
        self.connection.close()


if __name__ == '__main__':

    # for i in range(15):
    publish = Publish()
    publish.start_publish("发送第s个消息")
