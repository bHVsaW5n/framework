import time

# from base.日志.日志文件记录 import logger
from base.日志.file_logger import file_logger


def time_decorator(fun):
    def wrapper(*args, **key_words):
        try:
            start_time = time.time()
            # print(fun.__name__)
            # print("args", locals().get("args"))
            # print("key_words", locals().get("key_words"))
            # file_logger.info('{fun_name}方法调用的前端参数为{args}, {kewargs}'.format(
            #     **{"fun_name": fun.__name__,
            #        "args": locals().get("args"),
            #        "kewargs": key_words}))

            result = fun(*args, **key_words)
            end_time = time.time()
            print("运行时间:", (end_time - start_time)*100)
            return result
        except Exception as e:
            print(e)

    return wrapper


@time_decorator
def add(a, b):
    print(a ** b)


if __name__ == '__main__':
    add(2, 5)
