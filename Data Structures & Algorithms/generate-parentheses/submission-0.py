class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        def rec(cur, left, right):
            if not left and not right:
                out.append(cur)
                return
            if left:
                rec(cur + '(', left - 1, right)
            if right > left:
                rec(cur + ')', left, right - 1)
        
        rec('', n, n)
        return out
        