class Solution:
    def convertToBase7(self, num: int) -> str:
        negative = False
        if num == 0:
            return "0"
        if num < 0:
            num *= -1
            negative = True
        digits = []
        while num != 0:
            digits.append(num%7)
            num //= 7
        if negative:
            return f"-{''.join(map(str, digits[::-1]))}"
        else:
            return ''.join(map(str, digits[::-1]))
        