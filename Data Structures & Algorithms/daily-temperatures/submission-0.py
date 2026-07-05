class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[Tuple[int, int]] = []
        res: List[int] = [0 for _ in temperatures]

        for right, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, left = stack.pop()
                res[left] = right - left
            
            stack.append((temp, right))

        return res
