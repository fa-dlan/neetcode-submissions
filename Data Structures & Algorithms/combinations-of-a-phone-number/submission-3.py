class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        pq = dic[digits[0]].copy()
        for digit in digits[1:]:
            temp = []
            while pq:
                word = pq.pop()
                for appended_char in dic[digit]:
                    temp.append(word + appended_char)
            pq = temp

        return pq