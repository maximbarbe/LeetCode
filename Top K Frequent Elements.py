class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for val in nums:
            if freq.get(val, False) == False:
                freq[val] = 1
            else:
                freq[val] += 1
        heap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res