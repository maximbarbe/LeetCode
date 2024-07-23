class Solution:
    def tribonacci(self, n: int) -> int:
        if n in [0, 1, 2]:
            return 0 if n == 0 else 1
        x0 = 0
        x1 = 1
        x2 = 1
        for i in range(3, n + 1):
            cur = x0 + x1 + x2
            x0 = x1
            x1 = x2
            x2 = cur
        return x2