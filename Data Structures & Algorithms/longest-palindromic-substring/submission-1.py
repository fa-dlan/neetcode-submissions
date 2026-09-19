class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub == sub[::-1] and len(sub) > len(out):
                    out = sub
        return out