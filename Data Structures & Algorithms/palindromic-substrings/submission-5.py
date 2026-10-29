class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        out = 0

        # odd length palindrome centers at s[i]
        for i in range(n):
            offset = 0
            while (
                i - offset >= 0 and i + offset < n 
                and s[i - offset] == s[i + offset]
            ):
                out += 1
                offset += 1
        
        # odd length palindrome centers at s[i:i+2]
        for i in range(n - 1):
            offset = 0
            while (
                i - offset >= 0 and i + 1 + offset < n 
                and s[i - offset] == s[i + 1 + offset]
            ):
                out += 1
                offset += 1

        return out