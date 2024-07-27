class Solution:
    def dividing(self, num):
        temp = num
        while num != 0:
            digit = num % 10
            if digit == 0 or temp % digit != 0:
                return False
            num //= 10
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            if self.dividing(i):
                res.append(i)
        return res