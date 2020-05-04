"""
创建一堆数据
"""
from base.decorator import time_decorator
from model.chat import Chat
import time

datalist = [{"customer_service_id": 1, "customer_id": 2, "direction": 4, "content": "Dsfa_%s"%i} for i in range(10000)]

datalist1 = [{"customer_service_id": 1, "customer_id": 1, "direction": 0, "content": "Dsfa_%s"%i} for i in range(1000)]

@time_decorator
def insert_data_10000():
    Chat.insert_many(datalist).execute()

@time_decorator
def insert_data_1000():
    for i in range(10):
        Chat.insert_many(datalist).execute()

if __name__ == '__main__':
    insert_data_10000()
    # insert_data_1000()


