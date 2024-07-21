class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = [False]*(len(nums) + 1)
        for val in nums:
            seen[val] = True
        for v in range(len(seen)):
            if not seen[v]:
                return v