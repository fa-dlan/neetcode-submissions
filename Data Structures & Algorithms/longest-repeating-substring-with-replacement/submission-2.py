class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # pseudo:
        # every end of substring, extends by k, repeat the process
        n = len(s)
        out = 0

        left, right = 0, 0
        while left < n:
            cur_char = s[left]
            replace_count = k
            right = left
            cur_length = 0
            while right < n:
                if s[right] != cur_char:
                    if not replace_count:
                        break
                    replace_count -= 1
                elif left == right:
                    left += 1

                cur_length += 1
                right += 1

            if replace_count:
                cur_length = min(n, cur_length + replace_count)
            out = max(out, cur_length)
        
        return out