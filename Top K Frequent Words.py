class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        heap = [(-val, key) for key, val in c.items()]
        res = []
        heapq.heapify(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res