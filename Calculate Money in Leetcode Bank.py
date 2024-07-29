class Solution:
    def totalMoney(self, n: int) -> int:
        start = 0
        cur = 0
        res = 0
        for i in range(1, n+1):
            if (i - 1)%7 == 0:
                start += 1
                cur = start
            res += cur
            cur += 1
        return res