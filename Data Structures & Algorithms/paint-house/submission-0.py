class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
            
        dp = [[costs[0][0], costs[0][1], costs[0][2]]]

        for idx in range(1, len(costs)):
            dp.append([
                min(dp[-1][1],  dp[-1][2]) + costs[idx][0],
                min(dp[-1][0],  dp[-1][2]) + costs[idx][1],
                min(dp[-1][0],  dp[-1][1]) + costs[idx][2],
            ])

        return min(dp[-1])