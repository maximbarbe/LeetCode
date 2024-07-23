class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                num = sqrt(i**2 + j**2)
                if num <= n and floor(num) == num:
                    res += 1
        return res