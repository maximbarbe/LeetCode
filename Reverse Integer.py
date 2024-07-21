class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            negative = True
            t = str(x)[1:]
            res = int(f"-{t[::-1]}")

        else:
            res = int(f"{str(x)[::-1]}")
        if res < -2**31 or res > 2**31 - 1:
            return 0
        else:
            return res