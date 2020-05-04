class Foo:
    def __init__(self,name,count):
        self.name = name
        self.count = count
    def __hash__(self):
        print("%s调用了哈希方法"%self.name)
        return hash(self.count)
    def __eq__(self, other):
        print("%s调用了eq方法"%self.name)
        return self.__dict__ == other.__dict__

f1 = Foo('f1',1)
f2 = Foo('f2',1)
f3 = Foo('f3',3)
ls = [f1,f2,f3]
print(set(ls))