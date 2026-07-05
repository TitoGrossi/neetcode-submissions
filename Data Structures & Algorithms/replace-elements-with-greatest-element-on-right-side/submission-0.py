class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
            
        max_element = arr[-1]
        arr[-1] = -1
        
        for idx in range(len(arr) -  2, -1, -1):
            current = arr[idx]
            arr[idx] = max_element
            max_element = max(current, max_element)

        return arr
