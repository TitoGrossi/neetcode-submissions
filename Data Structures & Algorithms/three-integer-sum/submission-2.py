from collections import defaultdict
from typing import Tuple

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        response: Set[Tuple[int, ...]] = set()

        for idx, num in enumerate(nums):
            tuples = self.two_sum(-num, idx + 1, nums)
            for tup in tuples:
                tup.append(nums[idx])
                tup.sort()
                response.add(tuple(tup))

        return [list(tup) for tup in response]

    @staticmethod
    def two_sum(target: int, low: int, nums: List[int]):
        response: List[List[int]] = []
        high = len(nums) - 1

        while low < high:
            sum_low_high = nums[low] + nums[high]
            if sum_low_high > target:
                high -= 1
            elif sum_low_high < target:
                low += 1
            else:
                response.append([nums[low], nums[high]])
                high -= 1
                low += 1

        return response
