from base.decorator import time_decorator
from model.chat import Chat


class DatabaseTestService:
    def __init__(self):
        pass


    @time_decorator
    def get_data_from_db(self):
        chat_objs = Chat.select().where(Chat.direction == 4).order_by(Chat.direction.desc()).limit(50)
        datalist = [{"id": obj.id, "customer_id": obj.customer_id, "direction": obj.direction, "content": obj.content,
                     "gen_time": str(obj.gen_time)[:19]} for obj in chat_objs]
        count = len(datalist)
        return datalist, count


database_test_service = DatabaseTestService()