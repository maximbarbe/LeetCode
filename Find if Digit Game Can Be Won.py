class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit = 0
        double_digit = sum(nums)
        for v in nums:
            if v < 10:
                single_digit += v
                double_digit -= v
        return single_digit != double_digit