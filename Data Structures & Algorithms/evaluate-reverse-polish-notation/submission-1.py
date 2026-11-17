class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        operators = ('+', '-', '*', '/')
        def next():
            cur = tokens.pop()

            # cur is number
            if cur not in operators:
                return int(cur)

            # cur is an operator
            b = next()
            a = next()
            if cur == '+':
                return a + b
            elif cur == '-':
                return a - b
            elif cur == '*':
                return a * b
            elif cur == '/':
                return int(a / b)

        return next()