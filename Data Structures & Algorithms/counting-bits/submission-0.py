class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n + 1):
            cur = f'{i:b}'
            temp = 0
            for c in cur:
                if c == '1':
                    temp += 1
            out.append(temp)
        return out