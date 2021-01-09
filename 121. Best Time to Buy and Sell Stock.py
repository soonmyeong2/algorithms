class Solution(object):
    def maxProfit(self, prices):
        profit, low = 0, float('inf')
        
        for price in prices:
            low = min(price, low)
            profit = max(price - low, profit)
        return profit
