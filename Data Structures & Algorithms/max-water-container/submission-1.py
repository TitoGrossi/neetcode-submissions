class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low, high = 0, len(heights) - 1

        max_area = 0
        while low < high:
            max_area = max(max_area, (high - low) * min(heights[low], heights[high]))
            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1

        return max_area
