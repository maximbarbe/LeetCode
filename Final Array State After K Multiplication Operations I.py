class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, v in enumerate(nums):
            heapq.heappush(heap, (nums[i], i))
        for i in range(k):
            val, idx = heapq.heappop(heap)
            nums[idx] *= multiplier
            heapq.heappush(heap, (nums[idx], idx))
        return nums