class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n, 'b')
        while len(b) < 32:
            b = '0' + b
        return int(b[::-1], 2)