class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp= sorted(nums.copy())
        res = []
        for val in nums:
            res.append(bisect_left(temp, val))
        return res