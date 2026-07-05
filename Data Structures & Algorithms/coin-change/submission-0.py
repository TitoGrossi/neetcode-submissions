class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo: Dict[int, int] = {}
        
        def dfs(remaining: int) -> int:
            if remaining < 0:
                return amount + 1
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]

            memo[remaining] = 1 + min(
                dfs(remaining - coin) for coin in coins
            )

            return memo[remaining]

        res = dfs(amount)

        return res if res <= amount else -1
