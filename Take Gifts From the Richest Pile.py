class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gifts[i] for i in range(len(gifts))]
        heapq.heapify(heap)
        for i in range(k):
            cur = heapq.heappop(heap)
            heapq.heappush(heap, -floor(sqrt(-cur)))
        return -sum(heap)