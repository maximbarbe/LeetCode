class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum = sum(nums)
        digit_sum = 0
        for v in nums:
            cur = 0
            while v != 0:
                cur += v % 10
                v //= 10
            digit_sum += cur
        return abs(el_sum - digit_sum)