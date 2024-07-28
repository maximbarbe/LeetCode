class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            cur = set()
            for j in range(i, len(nums)):
                cur.add(nums[j])
                res += len(cur) ** 2
        return res