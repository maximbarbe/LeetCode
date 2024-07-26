class Solution:

    def subsets(self,nums, idx, cur, sub):
        if idx == len(nums):
            sub.append(cur)
            return
        self.subsets(nums, idx + 1, cur + [nums[idx]], sub)
        self.subsets(nums, idx + 1, cur, sub)
    def subsetXORSum(self, nums: List[int]) -> int:
        sub = []
        self.subsets(nums, 0, [], sub)
        res = 0
        for i in range(len(sub)):
            cur = 0
            for j in range(len(sub[i])):
                cur ^= sub[i][j]
            res += cur
        return res