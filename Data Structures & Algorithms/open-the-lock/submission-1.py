class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)
        queue = deque()
        if "0000" not in seen:
            queue.append(("0000", 0))
        seen.add("0000")
        
        while queue:
            combination, turns = queue.popleft()
            if combination == target:
                return turns

            for idx, digit in enumerate(combination):
                digit_repr = int(digit)
                for diff in (-1, 1):
                    new_comb = combination[:idx] + str((digit_repr + diff) % 10) + combination[idx+1:]
                    if new_comb not in seen:
                        seen.add(new_comb)
                        queue.append((new_comb, turns + 1))
        
        return -1
