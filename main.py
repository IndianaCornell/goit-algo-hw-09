import timeit


coins = [50, 25, 10, 5, 1]  

# Функція жадібного алгоритму
def find_coins_greedy(amount):
 
    coins.sort(reverse=True) 
    result = {}
    
    for coin in coins:
        for coin in coins:
            if amount >= coin:
                result[coin] = amount // coin
                amount %= coin
    return result

 
 


# Функція динамічного програмування
def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin != -1:
            if coin in result:
                result[coin] += 1
            else:
                result[coin] = 1
            amount -= coin
    
    return result




amounts = [10, 50, 100, 150, 300, 500]
res = []

for amount in amounts:
    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
    time_dp = timeit.timeit(lambda: find_min_coins(amount), number=1000)
    res.append([amount, time_greedy, time_dp])

print("Amount | Greedy Time (s) | DP Time (s)")
for result in res:
    print(f"{result[0]:>6} | {result[1]:>14.8f} | {result[2]:>12.8f}")