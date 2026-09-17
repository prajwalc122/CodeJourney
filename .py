# coin change greedy
coins = [10, 5, 2, 1]
amount = 18

result = []

for coin in coins:
    while amount >= coin:
        amount -= coin
        result.append(coin)

print(result)
