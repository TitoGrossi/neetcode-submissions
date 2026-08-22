class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low, high = 0, len(heights) - 1
        max_area = 0

        while low < high:
            area = min(heights[low], heights[high]) * (high - low)
            max_area = max(area, max_area)
            if heights[high] > heights[low]:
                low += 1
            else:
                high -= 1

        return max_area
