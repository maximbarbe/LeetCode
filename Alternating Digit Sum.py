class Solution:
    def alternateDigitSum(self, n: int) -> int:
        negative = False
        n = int(str(n)[::-1])
        digit_sum = 0
        while n != 0:
            dig = n % 10
            n //= 10
            if negative:
                digit_sum -= dig
            else:
                digit_sum += dig
            negative ^= True
        return digit_sum 