import string

from base.decorator import time_decorator
import time
import random
a = [random.choice(string.ascii_uppercase) for i in range(1000000)]
lll=time.time()
# print(a)
# a = ["Adsf", "dsf", "D", "Df", "dsf", "Sfa", "dfggg","DFgh","htr","fdg","zbcv","fdh","jtrh", "ASdf", "SDaf", "sdaf", "safd", "ASdf", "ASdf","Adsf", "dsf", "D", "Df", "dsf", "Sfa", "ASdf", "SDaf", "sdaf", "safd", "ASdf", "ASdf"]


@time_decorator
def aa():
    start = time.time()
    b = set(a)
    # time.sleep(1)
    end = time.time() - start
    print("aaa时间", end)
    return b

print("aaa", aa())

c = set()

@time_decorator
def bb():
    start = time.time()

    for i in a:
        c.add(i)
    # time.sleep(1)
    end = time.time() - start
    print("bbb时间", end)
    return c


print("bbb", bb())
print(time.time()-lll)