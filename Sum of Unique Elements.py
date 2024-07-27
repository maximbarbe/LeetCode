class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for key in c.keys():
            if c[key] == 1:
                res += key
        return res