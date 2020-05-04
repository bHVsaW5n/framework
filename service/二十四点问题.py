# EXP = {}
#
# def compute(x,y,op):
#     if op=='+':return x+y
#     elif op=='*':return x*y
#     elif op=='-':return x-y
#     else:return x/y if y else None
#
# def exp(array_n,target,iter=0):
#     if len(array_n)==1:return [(array_n[0],str(array_n[0]))]
#     operation = ['+','-','*','/']
#     ret = []
#     for num in range(1,len(array_n)):
#         exp1 = array_n[:num]
#         exp2 = array_n[num:]
#
#         ret1 = EXP[exp1] if exp1 in EXP else exp(exp1,target,iter+1)
#         ret2 = EXP[exp2] if exp2 in EXP else exp(exp2,target,iter+1)
#         EXP[exp1] = ret1
#         EXP[exp2] = ret2
#         for op in operation:
#             for va1,expression in ret1:
#                 if va1==None:continue
#                 for va2,expression2 in ret2:
#                     if va2==None:continue
#                     combined_exp = '{}{}' if expression.isalnum() else '({}){}'
#                     combined_exp += '{}' if expression2.isalnum() else '({})'
#                     new_val = compute(va1,va2,op)
#                     ret.append((new_val,combined_exp.format(expression,op,expression2)))
#                     if iter==0 and new_val==target:
#                         #print('ans')
#                         return ''.join(e for x,e in ret if x==target)
#     return ret if iter else None
# def search(array):
#     record = set()
#     from itertools import permutations
#     for p in permutations(array):
#         if p in record:continue
#         record.add(p)
#         ret = exp(tuple(p),100)
#         if ret:print(ret);break
# exp([2,3,4,11,1,3], 24)


# coding: utf-8

from __future__ import division
from itertools import combinations
import re


class Solver:

    # 需要达成的目标结果值
    target = 24

    # 四则运算符号定义，其中，a -- b = b - a，a // b = b / a
    ops = ['+', '-', '*', '/', '--', '//']

    # precise_mode为精准模式，若开启，则减号及除号后开启括号
    def __init__(self, precise_mode=False):
        self.precise_mode = precise_mode

    def solution(self, nums):
        result = []
        groups = self.dimensionality_reduction(self.format(nums))
        for group in groups:
            for op in self.ops:
                exp = self.assemble(group[0], group[1], op)['exp']
                if self.check(exp, self.target) and exp not in result:
                    result.append(exp)
        return [exp + '=' + str(self.target) for exp in result]

    # 对需要处理的数字或表达式组合进行降维，降低到二维
    def dimensionality_reduction(self, nums):
        result = []

        # 如果维数大于2，则选出两个表达式组合成一个，从而降低一个维度，通过递归降低到二维
        if len(nums) > 2:
            for group in self.group(nums, 2):
                for op in self.ops:
                    new_group = [self.assemble(group[0][0], group[0][1], op)] + group[1]
                    result += self.dimensionality_reduction(new_group)
        else:
            result = [nums]
        return result

    # 将两个表达式组合成一个新表达式
    def assemble(self, exp1, exp2, op):

        # 如果运算符为'--'或者'//'，则交换数字顺序重新计算
        if op == '--' or op == '//':
            return self.assemble(exp2, exp1, op[0])

        # 如果是乘法，则根据两个表达式的情况加括号
        if op in r'*/':
            exp1 = self.add_parenthesis(exp1)
            exp2 = self.add_parenthesis(exp2)

        if self.precise_mode:
            if op == '-':
                exp2 = self.add_parenthesis(exp2)
            elif op == '/':
                exp2 = self.add_parenthesis(exp2, True)

        exp = self.convert(exp1['exp'] + op + exp2['exp'], op)
        return {'op': op, 'exp': exp}

    # 根据需要为表达式添加相应的括号
    @staticmethod
    def add_parenthesis(exp, is_necessary=False):

        # 如果上一计算步骤的运算符号为加号或减号，则需加括号
        if (is_necessary and not exp['exp'].isdigit()) or exp['op'] in r'+-':
            result = {
                'exp': '(' + exp['exp'] + ')',
                'op': exp['op']
            }
        else:
            result = exp
        return result

    # 检查表达式是否与结果相等，考虑到中间步骤的除法，因此不采用相等判断，而是采用计算值和目标值的绝对值是否符合某个精度
    @staticmethod
    def check(exp, target, precision=0.0001):
        try:
            return abs(eval(exp) - target) < precision
        except ZeroDivisionError:
            return False

    # 将表达式各项重新排序成为等价标准表达式
    @staticmethod
    def convert(exp, op):
        if op in r'+-':
            pattern = r'([\+\-]((\(.+\)|\d+)[\*\/](\(.+\)|\d+)|\d+))'
            exp = '+' + exp
        else:
            pattern = r'([\*\/](\(.+?\)|\d+))'
            exp = '*' + exp
        result = ''.join(sorted([i[0] for i in re.findall(pattern, exp)]))
        if len(result) != len(exp):
            result = exp
        return result[1:]

    # 将输入的数字格式化为字典，数字的运算符号为空格，注意不是空字符
    @staticmethod
    def format(nums):
        return [{'op': ' ', 'exp': str(num)} for num in nums]

    # 对表达式列表进行分组，返回列表，[[[n1, n2], [n3, n4]], [[n1, n3], [n2, n4]], ...]
    @staticmethod
    def group(exp_list, counter):

        # 生成以下标号为元素的列表
        index_list = [i for i in range(len(exp_list))]

        # 以下标号列表取出不重复的组合
        combination = list(combinations(index_list, counter))

        # 使用下标得到原表达式并组成最终的结果数组
        for group1 in combination:
            group2 = list(set(index_list) - set(group1))
            yield [
                [exp_list[g1] for g1 in group1],
                [exp_list[g2] for g2 in group2]
            ]

auto_input = True
if auto_input:
    from numpy import random
    customer_input = random.randint(1, 20, size=4)
else:
    customer_input = list()
    customer_input.append(input('请输入第一个数字：'))
    customer_input.append(input('请输入第二个数字：'))
    customer_input.append(input('请输入第三个数字：'))
    customer_input.append(input('请输入第四个数字：'))

task = Solver()
# print(customer_input)
#
# may_list = []
# a = [i for i in range(1, 11)]
#
# for index_i in range(0, 10):
#     for index_j in range(index_i+1, 10):
#         for index_m in range(index_j+1, 10):
#             for index_n in range(index_m+1, 10):
#                 may_list.append([a[index_i], a[index_j], a[index_m], a[index_n]])

# for item in may_list:
answer = task.solution([4, 5, 8, 10])

if len(answer) == 0:
    print([4, 5, 8, 10], 'No solutions')
else:
    for a in answer:
        print([4, 5, 8, 10], a)