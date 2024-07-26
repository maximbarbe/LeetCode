class Solution:

    def comb(self, nums, target, res, idx, cur):
        if target < 0:
            return
        elif target == 0:
            res.append(cur)
            return
        else:
            if idx == len(nums):
                return
            self.comb(nums, target - nums[idx], res, idx, cur + [nums[idx]])

            self.comb(nums, target, res, idx + 1, cur)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.comb(candidates, target, res, 0, [])
        return res