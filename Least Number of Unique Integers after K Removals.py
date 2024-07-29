class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        heap = [(c[key], key) for key, value in c.items()]
        heapq.heapify(heap)
        while k != 0:
            count, num = heapq.heappop(heap)
            count -= 1
            k -= 1
            if count > 0:
                heapq.heappush(heap, (count, num))
        return len(heap)