class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s:
            return 0
        n = len(s)
        memo = {}

        def r(left, cur, rem):
            if (left, cur, rem) in memo:
                return memo[(left, cur, rem)]

            if not rem:
                return 1 if cur == t else 0

            out = 0
            for i in range(left, n):
                out += r(i + 1, cur + s[i], rem - 1)

            memo[(left, cur, rem)] = out
            return out

        out = 0
        for i in range(n):
            out += r(i + 1, s[i], len(t) - 1)

        return out