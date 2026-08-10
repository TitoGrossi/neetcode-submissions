class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.get_row(matrix=matrix, target=target)
        if row is None:
            return False

        return self.binary_search(matrix[row], target)

    @staticmethod
    def get_row(matrix: List[List[int]], target: int) -> Optional[int]:
        low, high = 0, len(matrix) - 1
        while low <= high:
            midd = (low + high) // 2
            lower_bound, higher_bound = matrix[midd][0], matrix[midd][len(matrix[0]) - 1]

            if lower_bound <= target <= higher_bound:
                return midd
            elif target < lower_bound:
                high = midd - 1
            else:
                low = midd + 1

        return None

    @staticmethod
    def binary_search(array: List[int], target: int) -> bool:
        low, high = 0, len(array) - 1

        while low <= high:
            midd = (low + high) // 2
            if array[midd] == target:
                return True
            elif target  > array[midd]:
                low = midd + 1
            else:
                high = midd - 1

        return False
