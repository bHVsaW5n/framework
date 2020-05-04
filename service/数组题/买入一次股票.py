# prices = [7, 1, 5, 3, 6, 4, 7, 9, 3, 7, 4, 8]
prices = [3,9,1,5]
def max_price(prices):
    maxprofix = 0
    min_price = 1000
    for price in prices:
        maxprofix = max(maxprofix, price - min_price)
        if price < min_price:
            min_price = price
    return maxprofix

print(max_price(prices))