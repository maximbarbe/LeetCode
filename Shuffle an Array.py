class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.copy = self.nums.copy()
    def reset(self) -> List[int]:
        self.nums = self.copy.copy()
        return self.nums
    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()