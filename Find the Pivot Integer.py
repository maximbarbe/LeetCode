class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 1
        right = (n * (n+1))//2
        if left == right:
            return 1
        for i in range(2, n + 1):
            left += i
            right -= (i -1)
            if left == right:
                return i
        return -1