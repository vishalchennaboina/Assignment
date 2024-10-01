def min_coins(coins, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, target_sum + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[target_sum] if dp[target_sum] != float('inf') else -1

#Example
print(min_coins([25, 10, 5], 30))
print(min_coins([9, 6, 5, 1], 19))
print(min_coins([5, 1], 0))
print(min_coins([4, 6, 2], 5))