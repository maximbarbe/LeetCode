class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) % 2 == 1:
            res = 0
            for v in nums:
                res += abs(nums[len(nums) // 2] - v)
            return res
        else:
            r1, r2 = 0, 0
            for v in nums:
                r1 += abs(nums[len(nums) // 2] - v)
                r2  +=abs(nums[len(nums) // 2 - 1] - v)
            return min(r1, r2)