class Solution:

    def subset(self, nums, idx, subsets, cur):
        if idx == len(nums):
            subsets.add(tuple(cur))
            return
        self.subset(nums, idx + 1, subsets, cur + [nums[idx]])
        self.subset(nums, idx + 1, subsets, cur)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = set()
        self.subset(nums, 0, subsets, [])

        return list(map(list, subsets))