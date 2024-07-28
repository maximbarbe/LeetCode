class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        intersect = [False] * 101
        for start, end in nums:
            for i in range(start, end + 1):
                intersect[i] = True
        res = 0
        for i in range(101):
            if intersect[i]:
                res += 1
        return res