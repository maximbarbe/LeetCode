class Solution:
    def isPalindromic(self, n, base):
        nums = []
        while n != 0:
            nums.append(n % base)
            n //= base
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            if not self.isPalindromic(n, i):
                return False
        return True