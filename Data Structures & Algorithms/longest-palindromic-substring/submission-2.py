class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        out = s[0]

        for i in range(len(s)):
            # even left
            if i - 1 >= 0 and s[i] == s[i-1]:
                cur = s[i-1: i+1]
                k = 0
                while (i-1-k >= 0 
                        and i + k < len(s)
                        and s[i-1-k] == s[i+k]
                ):
                    cur = s[(i-1)-k: (i+k)+1]
                    if len(cur) > len(out):
                        out = cur
                    k += 1

            # even right
            if i + 1 < len(s) and s[i] == s[i+1]:
                cur = s[i: i+2]
                k = 0
                while (i-k >= 0 
                        and i+1+k < len(s)
                        and s[i-k] == s[i+1+k]
                ):
                    cur = s[i-k: (i+1+k)+1]
                    if len(cur) > len(out):
                        out = cur
                    k += 1
            
            # odd
            if (i - 1 >= 0
                and i + 1 < len(s)
                and s[i-1] == s[i+1]
            ):
                cur = s[i-1: i+2]
                k = 0
                while (i-1-k >= 0 
                        and i+1+k < len(s)
                        and s[i-1-k] == s[i+1+k]
                ):
                    cur = s[i-1-k: (i+1+k)+1]
                    if len(cur) > len(out):
                        out = cur
                    k += 1
        return out                