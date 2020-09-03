class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
