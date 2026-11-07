class PrefixTree:

    def __init__(self):
        self.m = {}
        self.s = set()

    def insert(self, word: str) -> None:
        self.s.add(word)
        cur = self.m
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]

    def search(self, word: str) -> bool:
        return word in self.s

    def startsWith(self, prefix: str) -> bool:
        cur = self.m
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True