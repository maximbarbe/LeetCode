class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = x
        digits = 0
        while temp != 0:
            digits += temp % 10
            temp //= 10
        if x % digits == 0:
            return digits
        return -1