class Solution:

    def comb(self, nums, idx, k, res, cur):
        if len(cur) == k:
            res.append(cur)
            return
        if idx == len(nums):
            return
        self.comb(nums, idx + 1, k, res, cur + [nums[idx]])
        self.comb(nums, idx + 1, k, res, cur)

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(1, n+1)]
        self.comb(nums, 0, k, res, [])
        return res