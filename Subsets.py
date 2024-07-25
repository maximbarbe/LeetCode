class Solution:

    def powerset(self, nums, idx, res, cur):
        if idx == len(nums):
            res.append(cur)
        else:
            self.powerset(nums, idx + 1, res, cur + [nums[idx]])
            self.powerset(nums, idx + 1, res, cur)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.powerset(nums, 0, res, [])
        return res