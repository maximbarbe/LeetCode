class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        for i in range(len(digits)):
            digits[i] += 1
            if digits[i] < 10:
                break
            else:
                digits[i] = 0
        else:
            digits.append(1)
        return digits[::-1]