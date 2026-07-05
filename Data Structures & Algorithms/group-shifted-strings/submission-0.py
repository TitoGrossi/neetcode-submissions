from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        max_length = max(len(string) for string in strings)
        
        families = defaultdict(lambda: [])

        for string in strings:
            char_dists = [-1 for _ in range(max_length - 1)]
            for idx in range(1, len(string)):
                char_dists[idx-1] = calc_char_dist(string[idx-1], string[idx])
            
            families[tuple(char_dists)].append(string)

        return [family for family in families.values()]
        


def calc_char_dist(char1: str, char2: str) -> int:
    char1_value = ord(char1)
    char2_value = ord(char2)

    return (char2_value - char1_value) % 26
