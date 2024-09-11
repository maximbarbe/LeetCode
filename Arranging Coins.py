class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 1, 2**31 - 1
        while start < end:
            mid = (start + end)//2
            val = (mid * (mid + 1))//2
            if val == n:
                return mid
            elif val < n:
                start = mid + 1
            else:
                end = mid - 1
        if (start * (start+1))//2 > n:
            return start - 1
        else:
            return start