prices = [7, 1, 5, 3, 6, 4, 7, 9, 3, 7, 4, 8]


def maxProfit(self, prices):
    in_list = []
    out_list = []
    min_value = -1
    max_value = 10000
    length = len(prices)
    for index, price in enumerate(prices):
        if index + 1 < length:
            if price < prices[index+1]:  # 当前值的后续有值比他大
                in_list.append((index, price))





