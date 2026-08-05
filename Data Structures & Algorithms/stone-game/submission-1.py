class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles) - 1
        total_points = sum(piles)

        memo = {}

        def dfs(low: int, high: int):
            if low >= high:
                return 0

            is_allice_turn = (low + (n - high)) % 2 == 0

            if (low, high) in memo:
                return memo[(low, high)]

            memo[(low, high)] = max(
                dfs(low + 1, high) + piles[low] * is_allice_turn,
                dfs(low, high - 1) + piles[high] * is_allice_turn,
            )

            return memo[(low, high)]

        allice_optimal_points = dfs(0, len(piles) - 1)

        return allice_optimal_points * 2 > total_points
