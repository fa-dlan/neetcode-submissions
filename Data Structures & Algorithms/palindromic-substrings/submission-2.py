class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i] = number of palindrome that starts at i, 
        if not s:
            return 0
        n = len(s)
        out = 0

        # odd length palindrome
        for i in range(n):
            offset = 0
            while (
                i - offset >= 0 and i + offset < n 
                and s[i - offset] == s[i + offset]
            ):
                out += 1
                offset += 1
        
        # even length palindrome
        for i in range(n):
            offset = 0
            while (
                i - offset >= 0 and i + 1 + offset < n 
                and s[i - offset] == s[i + 1 + offset]
            ):
                out += 1
                offset += 1
        return out