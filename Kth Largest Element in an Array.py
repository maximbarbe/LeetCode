class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda el: -el, nums))
        heapq.heapify(nums)

        for i in range(k):
            cur = heapq.heappop(nums)
        return -cur