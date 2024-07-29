class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i, len(nums)):
                cur = gcd(cur, nums[j])
                if cur < k:
                    break
                elif cur == k:
                    res += 1
        return res