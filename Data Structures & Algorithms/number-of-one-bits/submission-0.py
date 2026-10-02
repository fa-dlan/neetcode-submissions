class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        b = format(n, 'b')
        for c in b:
            if c == '1':
                out += 1
        return out