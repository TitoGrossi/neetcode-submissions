class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0

        for right, price in enumerate(prices):
            if price < prices[left]:
                left = right
            else:
                profit = max(profit, price - prices[left])

        return profit
