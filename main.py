import timeit

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            result[coin] = num_coins
            amount -= coin * num_coins
    return result

print(find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}


def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
                
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
        
    return result

# Приклад використання:
print(find_min_coins(113))  # {50: 2, 10: 1, 2: 1, 1: 1}

# Порівняння часу виконання
def compare_execution_time(amount):
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
    dp_time = timeit.timeit(lambda: find_min_coins(amount), number=1000)
    
    return greedy_time, dp_time

# Приклад використання та порівняння часу виконання
amounts = [113, 1000, 5000, 10000, 20000]
results = []

for amount in amounts:
    greedy_time, dp_time = compare_execution_time(amount)
    results.append((amount, greedy_time, dp_time))

print("| Amount | Greedy Time (s) | DP Time (s) |")
print("|--------|-----------------|-------------|")
for result in results:
    print(f"| {result[0]:>6} | {result[1]:>15.8f} | {result[2]:>11.8f} |")
