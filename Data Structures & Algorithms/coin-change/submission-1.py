class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp: list[int] = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0

        for remaining in range(1, len(dp)):
            for coin in coins:
                if remaining - coin >= 0 and dp[remaining - coin] != amount + 1:
                    dp[remaining] = min(dp[remaining], dp[remaining - coin] + 1)

        return dp[-1] if dp[-1] <= amount else -1
