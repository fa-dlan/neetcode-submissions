class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        out_left = 0
        out_right = 0

        for i in range(len(s)):
            # even left
            if i - 1 >= 0 and s[i] == s[i-1]:
                k = 0
                while (i-1-k >= 0 
                        and i + k < len(s)
                        and s[i-1-k] == s[i+k]
                ):
                    cur_left = i-1-k
                    cur_right = i+k

                    if cur_right - cur_left > out_right - out_left:
                        out_left = cur_left
                        out_right = cur_right

                    k += 1

            # even right
            if i + 1 < len(s) and s[i] == s[i+1]:
                k = 0
                while (i-k >= 0 
                        and i+1+k < len(s)
                        and s[i-k] == s[i+1+k]
                ):
                    cur_left = i-k
                    cur_right = i+1+k

                    if cur_right - cur_left > out_right - out_left:
                        out_left = cur_left
                        out_right = cur_right

                    k += 1
            
            # odd
            if (i - 1 >= 0
                and i + 1 < len(s)
                and s[i-1] == s[i+1]
            ):
                k = 0
                while (i-1-k >= 0 
                        and i+1+k < len(s)
                        and s[i-1-k] == s[i+1+k]
                ):
                    cur_left = i-1-k
                    cur_right = i+1+k

                    if cur_right - cur_left > out_right - out_left:
                        out_left = cur_left
                        out_right = cur_right

                    k += 1

        return s[out_left:out_right+1]