class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = list(map(tuple, points))
        visited = defaultdict(lambda:False)
        heap = [(inf, points[i][0], points[i][1]) for i in range(len(points))]
        heap[0] = (0, heap[0][1], heap[0][2])
        res = 0
        while heap != []:
            cur, x, y = heapq.heappop(heap)
            res += cur
            for i in range(len(heap)):
                distance = abs(x - heap[i][1]) + abs(y - heap[i][2])
                if distance < heap[i][0]:
                    heap[i] = (distance, heap[i][1], heap[i][2])
            heapq.heapify(heap)
        return res