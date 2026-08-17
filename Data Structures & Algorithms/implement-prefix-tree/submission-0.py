from typing import Union

Trie = Dict[str, Union["Trie", str] ]

class PrefixTree:
    __end_symbol = "*"

    def __init__(self):
        self.trie: Trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

        node["*"] = {}

    def search(self, word: str) -> bool:
        node = self.__travel(word)
        return node is not None and self.__end_symbol in node

    def startsWith(self, prefix: str) -> bool:
        node = self.__travel(prefix)
        return node is not None

    def __travel(self, prefix: str) -> Optional[Trie]:
        node = self.trie
        for char in prefix:
            if char not in node:
                return None
            node = node[char]

        return node
        