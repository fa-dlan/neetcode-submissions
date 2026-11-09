class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        m, n = len(s), len(t)
        i, j = 0, 0

        for j in range(n):
            if t[j] == s[i]:
                i += 1
            if i == m:
                return True
        return False