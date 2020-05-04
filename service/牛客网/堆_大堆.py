class HeapMax:
    def __init__(self):
        self.data = []
        self.count = 0

    def add(self, value):
        this_value_index = self.count  # 当前这个插入值的索引
        self.data.append(value)  # 将元素插入
        parent_index = (this_value_index-1) // 2  # 父节点的索引
        while this_value_index >= 0 and parent_index>=0 and self.data[parent_index] < self.data[this_value_index]:
            temp = self.data[parent_index]
            self.data[parent_index] = self.data[this_value_index]  # 当前节点和父节点换位置
            self.data[this_value_index] = temp
            this_value_index = parent_index
            parent_index = (this_value_index-1) // 2
        self.count += 1

    def get_max(self):
        if self.count == 0:
            return None
        elif self.count > 0:
            max = self.data.pop(0)
            self.count -= 1
            if self.count > 1:
                self.data.insert(0, self.data[-1])  # 最后一个插入到根位置
                self.data.pop(-1)  # 最后一个删除
                this_index = 0
                left_child = 2 * this_index + 1
                right_child = 2 * this_index + 2
                while left_child < self.count and right_child < self.count:  # 当这个节点有孩子节点
                    if self.data[this_index] >= self.data[left_child] and self.data[this_index] >= self.data[right_child]:
                        break  # 如果当前节点比两个孩子节点都大，则退出
                    else:
                        if self.data[left_child] > self.data[right_child]:  # 左孩子大一点,跟左孩子换
                            temp = self.data[left_child]
                            self.data[left_child] = self.data[this_index]
                            self.data[this_index] = temp
                            this_index = left_child

                        else:
                            temp = self.data[right_child]
                            self.data[right_child] = self.data[this_index]
                            self.data[this_index] = temp
                            this_index = right_child
                        left_child = 2 * this_index + 1
                        right_child = 2 * this_index + 2
                if left_child < self.count:
                    if self.data[this_index] < self.data[left_child]:
                        temp = self.data[left_child]
                        self.data[left_child] = self.data[this_index]
                        self.data[this_index] = temp

            return max

    def __str__(self):
        super()
        s = "大根堆：" + "".join(str(self.data))

        # print(self.data)
        return s


if __name__ == '__main__':
    heap_max = HeapMax()
    for i in [3, 8, 3, 1, 2, 4, 5, 5, 6]:
        heap_max.add(i)
        print(heap_max)

    max_1 = heap_max.get_max()
    print(max_1)
    print(heap_max)
    max_2 = heap_max.get_max()
    print(max_2)
    print(heap_max)