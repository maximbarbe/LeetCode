class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = list(map(lambda el: -el, nums))
        heapq.heapify(heap)
        return (heapq.heappop(heap) +1) * (heapq.heappop(heap) + 1)