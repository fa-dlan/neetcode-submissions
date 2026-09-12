from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for char in s:
            if char in (')', ']', '}'):
                if not stack:
                    return False
                top = stack.pop()
                if (char == ')' and top != '('
                    or char == ']' and top != '['
                    or char == '}' and top != '{'
                ):
                    return False
            else:
                stack.append(char)
        return not stack