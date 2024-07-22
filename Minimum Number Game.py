class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 2):
            x1 = nums[i]
            x2 = nums[i + 1]
            res.append(x2)
            res.append(x1)
        return res