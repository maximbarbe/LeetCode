class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1, num + 1):
            digit_sum = 0
            while i != 0:
                digit_sum += i % 10
                i //= 10
            if digit_sum % 2 == 0:
                res += 1
        return res