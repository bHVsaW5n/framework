# from service.test import MessageHelper
#
#
# class Publish:
#     def __init__(self):
#         pass
#     def publish(self, message):
#         message_queue_service = MessageHelper()
#         message_queue_service.message_queue.append(3)
#         message_queue_service.message_queue.append(message)
#
# publisher = Publish()
# publisher.publish("bb")
import time

from service.test import Publish

pub = Publish()

# while True:
#     pub.publish({"fun": "add", "param": {"a": 3, "b": 4}})
#     time.sleep(3)
#     pub.publish({"fun": "print_str", "param": {"content": "content"}})
#     time.sleep(3)

pub.publish({"fun": "add", "param": {"a": 3, "b": 4}})