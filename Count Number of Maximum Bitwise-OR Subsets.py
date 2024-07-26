class Solution:
    def subsets(self, nums, idx, cur, subset):
        if idx == len(nums):
            subset.append(cur)
        else:
            self.subsets(nums, idx + 1, cur + [nums[idx]], subset)
            self.subsets(nums, idx + 1, cur, subset)
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        subset = []
        self.subsets(nums, 0, [], subset)
        max = -inf
        count = 0
        for i in range(len(subset)):
            cur = 0
            for j in range(len(subset[i])):
                cur |= subset[i][j]
            if cur > max:
                max = cur
                count = 1
            elif cur == max:
                count += 1
        return count