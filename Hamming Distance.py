class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        if len(x) < len(y):
            x = x.zfill(len(y))
        if len(y) < len(x):
            y = y.zfill(len(x))

        res = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                res += 1
        return res