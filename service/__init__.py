# def singleton(cls):
#     classes = {}
#     def getinstance(*args, **kwargs):
#         if cls not in classes:
#             classes[cls] = cls(*args, **kwargs)
#         return classes[cls]
#
#     return getinstance
#
#
# @singleton
# class my_cls(object):
#     pass
#
#
# my_clsd = my_cls()
# print(my_clsd)
#
# ss = my_cls()
# print(ss)
#
# def avg():
#     sum = 0
#     length = 0
#     def add_num(x):
#         nonlocal sum
#         nonlocal length
#         sum += x
#         length += 1
#         return sum / length
#     return add_num
# get_avg = avg()
#
# print(get_avg(5))
# print(get_avg(6))
