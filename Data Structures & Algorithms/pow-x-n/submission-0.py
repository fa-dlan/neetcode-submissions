class Solution:
    def myPow(self, x: float, n: int) -> float:
        # for sure O(log(n))
        # binary exponentiation?
        out = 1
        cur_exp = x

        is_neg = False
        if n < 0:
            n = n * -1
            is_neg = True

        while n:
            if n % 2 == 1:
                out  = out * cur_exp
            cur_exp = cur_exp * cur_exp
            n >>= 1

        if is_neg:
            return 1 / out
        return out