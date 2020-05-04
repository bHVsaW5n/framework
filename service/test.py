from threading import Thread

import time
import queue

message_queue = queue.Queue()
key = "1"

class Func:
    def add(self, param):
        a = param.get("a")
        b = param.get("b")
        print(a + b)
        return a + b

    def print_str(self, param):
        content = param.get('content')
        print(content)


func = Func()


class Consume:
    def __init__(self, key):
        self.key = key

    def start_consume(self):
        global message_queue
        global key
        while True:
            if message_queue and self.key == key:
                # print(message_queue.get())
                content = message_queue.get()
                fun = content['fun']
                param = content['param']
                print("self.key", self.key)
                getattr(func, fun)(param)
                if key == "1":
                    key = "2"
                else:
                    key = "1"
            # message_queue = message_helper.message_queue


def init_consumert(key):
    a = Consume(key)
    a.start_consume()


class Publish:
    def __init__(self):
        pass

    def publish(self, message):
        global message_queue

        message_queue.put(message)


thr1 = Thread(target=init_consumert, args=("1"))
thr1.start()


thr2 = Thread(target=init_consumert, args=("2"))
thr2.start()


pub = Publish()

while True:
    pub.publish({"fun": "add", "param": {"a": 3, "b": 4}})
    time.sleep(3)
    pub.publish({"fun": "print_str", "param": {"content": "content"}})
    time.sleep(3)


