from typing import Tuple

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0 for _ in temperatures]

        stack: List[Tuple[int, int]] = []
        for idx, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                _, eliminated_idx = stack.pop()
                results[eliminated_idx] = idx - eliminated_idx

            stack.append((temperature, idx))

        return results