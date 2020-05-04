import numpy as np
import random

area = np.zeros(shape=(10, 10), dtype=np.int)

init_head = (3, 4)  # 初始化蛇头部位置
area[init_head] = 1  # 头部位置设置为1

snake = [init_head]  # 蛇身


def get_seed():
    """
    获取种子，种子在地图内，且不在蛇身上
    :return:
    """
    seed = (random.randint(0, 9), random.randint(0, 9))
    while seed in snake:
        seed = (random.randint(0, 9), random.randint(0, 9))
    area[seed] = 2
    return seed


seed = get_seed()  # 获取果子


def eat_seed(head):
    """
    蛇头位置更新为当前位置
    蛇吃果子，如果蛇头与果子位置一致，则为吃到，身体长一格，尾巴不去掉， 原来果子位置变为蛇位置，再次重新获取果子， 果子位置为2
    没吃到果子，尾巴去掉一格，表明蛇仅移动了一个位置
    更新地图，蛇头位置为1，根据情况，尾巴设置为0
    :param head:
    :return:
    """
    if head in snake:
        raise Exception("吃到自己啦~")
    snake.insert(0, head)  # 蛇头位置更新
    if area[head] == 2:  # 果子，蛇吃了
        global seed
        seed = get_seed()

    else:  # 没吃到果子，尾巴去掉一个
        tail = snake.pop(-1)
        area[tail] = 0  # 蛇尾变为 0
    area[head] = 1  # 地图上蛇头位置变为1


def snake_eat_seed(direction):
    head = snake[0]  # 贪吃蛇的头
    if head[0] < 0 or head[0] > 9 or head[1] < 0 or head[1] > 9:
        raise Exception("撞墙啦~")
    else:
        if direction == 'l':
            new_head_x, new_head_y = head[0] - 1, head[1]  # 头部新位置
            if new_head_x < 0:
                raise Exception("往左撞到墙啦~")
            new_head = (new_head_x, new_head_y)
            eat_seed(new_head)
        if direction == "r":
            new_head_x, new_head_y = head[0] + 1, head[1]  # 头部新位置
            if new_head_x > 9:
                raise Exception("往右撞到墙啦~")
            new_head = (new_head_x, new_head_y)
            eat_seed(new_head)
        if direction == 'u':
            new_head_x, new_head_y = head[0], head[1] - 1  # 头部新位置
            if new_head_y < 0:
                raise Exception("往上撞到墙啦~")
            new_head = (new_head_x, new_head_y)
            eat_seed(new_head)
        if direction == 'd':
            new_head_x, new_head_y = head[0], head[1] + 1  # 头部新位置
            if new_head_y > 9:
                raise Exception("往下撞到墙啦~")
            new_head = (new_head_x, new_head_y)
            eat_seed(new_head)


if __name__ == '__main__':
    direction_list = ['l', 'r', 'u', 'd']
    print(seed, snake)
    while True:  # 从控制台输入方向，控制蛇往哪里移动
        direction_input = input("请输入方向")
        if direction_input in direction_list:
            snake_eat_seed(direction_input)
            print(direction_input, seed, snake)
        else:
            break
