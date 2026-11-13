class CountSquares:

    def __init__(self):
        self.d = {}

    def add(self, point: List[int]) -> None:
        p = tuple(point)
        self.d[p] = self.d.get(p, 0) + 1

    @staticmethod
    def slope(a, b):
        if not b[0] - a[0]:
            return float('inf')
        return (b[1] - a[1]) / (b[0] - a[0])
     
    def count(self, point: List[int]) -> int:
        a = tuple(point)
        out = 0
        for b, p2 in self.d.items():
            slp = self.slope(a, b)
            if slp not in (-1, 1):
                continue

            c = (a[0], b[1])
            d = (b[0], a[1])
            p3 = self.d.get(c, 0)
            p4 = self.d.get(d, 0)
            out += p2 * p3 * p4

        return out
    
    