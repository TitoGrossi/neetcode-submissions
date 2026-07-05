class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List[Tuple[int, int]] = []

        max_area = 0
        for right, height in enumerate(heights):
            start_idx = right
            while stack and stack[-1][0] > height:
                min_height, start_idx = stack.pop()
                max_area = max(max_area, (right - start_idx) * min_height)
            
            stack.append((height, start_idx))
        
        for height, start_idx in stack:
            right = len(heights) - 1
            max_area = max(max_area, (right - start_idx + 1) * height)

        return max_area