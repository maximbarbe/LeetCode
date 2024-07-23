class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 1, num
        if num == 1:
            return True
        while start < end:
            mid = (start + end)//2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                start = mid + 1
            else:
                end = mid
        return False