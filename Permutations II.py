from typing import List
class Solution:
    def perm(self, nums, idx, res):
        if idx == len(nums) - 1:
            res.add(tuple(nums))
        else:
            for i in range(idx + 1, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                self.perm(nums, i, res)
                nums[idx], nums[i] = nums[i], nums[idx]
            res.add(tuple(nums))
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        self.perm(nums, 0, res)
        return list(map(list, res))
sol = Solution()
print(sol.permuteUnique([1,2,3]))