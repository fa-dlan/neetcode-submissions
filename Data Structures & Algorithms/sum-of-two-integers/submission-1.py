class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFF
        N = 16

        # Convert to 16-bit two's complement
        a_bin = f'{a & MASK:016b}'
        b_bin = f'{b & MASK:016b}'

        out = []
        carry = 0

        # Binary addition from right to left
        for i in range(N - 1, -1, -1):
            bit_a = int(a_bin[i])
            bit_b = int(b_bin[i])

            total = bit_a ^ bit_b ^ carry
            carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b))

            out.append(str(total))

        # Reverse and convert to unsigned integer
        result = int(''.join(out[::-1]), 2)

        # Convert unsigned to signed two's complement
        if result & (1 << 15):
            result = ~(result ^ MASK)

        return result