class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = [False] * (len(nums))
        for val in nums:
            seen[val - 1] = True
        res = []
        for i in range(len(seen)):
            if not seen[i]:
                res.append(i + 1)
        return res