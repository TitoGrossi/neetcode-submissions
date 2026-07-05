class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not self._is_valid(words):
            return ""

        graph, in_edges = self._build_graph(words)

        queue: Deque[str] = deque([
            char for char, in_count in in_edges.items() if in_count == 0
        ])

        res: List[str] = []
        while queue:
            char = queue.popleft()
            res.append(char)
            for dep in graph[char]:
                in_edges[dep] -= 1
                if in_edges[dep] == 0:
                    queue.append(dep)

        return "".join(res) if len(res) == len(in_edges) else ""

    @staticmethod
    def _is_valid(words: List[str]) -> bool:
        for word_idx in range(len(words) - 1):
            if (
                len(words[word_idx]) > len(words[word_idx + 1])
                and words[word_idx][:len(words[word_idx + 1])] == words[word_idx + 1]
            ):
                return False

        return True

    @staticmethod
    def _build_graph(
        words: List[str],
    ) -> tuple[Dict[str, List[str]], Dict[str, int]]:
        graph: Dict[str, List[str]] = defaultdict(list)
        in_edges: Dict[str, int] = {}
        for word in words:
            for char in word:
                in_edges[char] = 0

        for word_idx in range(len(words) - 1):
            for char_idx in range(min(len(words[word_idx]), len(words[word_idx + 1]))):
                if words[word_idx][char_idx] != words[word_idx + 1][char_idx]:
                    graph[words[word_idx][char_idx]].append(words[word_idx + 1][char_idx])
                    in_edges[words[word_idx + 1][char_idx]] += 1
                    break

        return graph, in_edges
