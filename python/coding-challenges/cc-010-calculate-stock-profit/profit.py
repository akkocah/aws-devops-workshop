prices = [9, 11, 8, 5, 7, 10]

def m_profit(prices):
    result = 0
    for i in range(len(prices)-1):
        result = max(result, max(prices[i+1:]) - prices[i])
    return result

print(m_profit(prices))

###################################################

lst = [10, 20, 23, 22, 17, 30]
def buy_and_sell(lst):
    max_profit = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[j] - lst[i] > max_profit:
                max_profit = lst[j] - lst[i]
    return max_profit