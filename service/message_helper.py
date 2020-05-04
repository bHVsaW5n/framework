from sanic import Sanic


def singleton(cls):
    classes = {}
    def getinstance(*args, **kwargs):
        if cls not in classes:
            classes[cls] = cls(*args, **kwargs)
        return classes[cls]

    return getinstance



@singleton
class MessageHelper:
    def __init__(self):
        self.message_queue = []


import time
# app = Sanic()
if __name__ == "__main__":
    message_helper = MessageHelper()
    while True:
        time.sleep(50)
    # app.run(host="172.16.77.223", port=9000)
