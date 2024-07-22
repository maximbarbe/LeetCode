class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        seen = dict()
        for i in range(len(nums)):
            if seen.get(nums[i], 0) == 0:
                seen[nums[i]] = 1
            else:
                res += seen[nums[i]]
                seen[nums[i]] += 1
        return res