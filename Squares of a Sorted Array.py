class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        c = [0] * (10001)
        for i in range(len(nums)):
            c[abs(nums[i])] += 1
        idx = 0
        for i in range(len(nums)):
            while c[idx] == 0:
                idx += 1
            nums[i] = idx ** 2
            c[idx] -= 1
        return nums