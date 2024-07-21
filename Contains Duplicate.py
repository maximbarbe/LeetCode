class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for n in nums:
            if seen.get(n, False) == True:
                return True
            else:
                seen[n] = True
        else:
            return False