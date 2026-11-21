class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits

        i = len(digits) - 1
        while digits[i] == 9 and i >= 0:
            digits[i] = 0
            i -= 1

        if i == -1:
            digits.insert(0, 1)
        else:
            digits[i] += 1
        return digits