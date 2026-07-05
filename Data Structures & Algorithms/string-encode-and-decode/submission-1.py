class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lengths: List [str] = []
        for string in strs:
            lengths.append(len(string))


        return ",".join(map(str, lengths)) + " " + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
            
        recorded_lengths, strs = s.split(" ", 1)
        boundaries: List[Tuple[int, int]] = []
        for l in recorded_lengths.split(","):
            begin = 0 if not boundaries else boundaries[-1][1]
            boundaries.append((begin, begin + int(l)))

        decoded: List[str] = []
        for begin, end in boundaries:
            decoded.append(strs[begin:end])

        return decoded
