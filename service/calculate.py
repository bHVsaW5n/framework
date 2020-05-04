class Stack(object):

    def __init__(self):
     # 创建空列表实现栈
        self.__list = []

    def is_empty(self):
    # 判断是否为空
        return self.__list == []
    def push(self,item):
    # 压栈，添加元素
        self.__list.append(item)

    def pop(self):
    # 弹栈，弹出最后压入栈的元素
        if self.is_empty():
            return
        else:
            return self.__list.pop()

    def top(self):
    # 取最后压入栈的元素
        if self.is_empty():
            return
        else:
            return self.__list[-1]
stack = Stack()
result = None
expression = "((5+4)*((2-1)*(3-1)/2))"
for i in expression:
    if i != ")":
        stack.push(i)
    else:
        part_str = []
        while not stack.is_empty():
            s = stack.pop()
            if stack.is_empty():
                print("结果：", result)
            if s != '(':
                part_str.append(s)
            else:
                s = ''.join(reversed(part_str))
                num = eval(s)
                num = str(num)
                stack.push(num)
                part_str = []
                result = num
                break