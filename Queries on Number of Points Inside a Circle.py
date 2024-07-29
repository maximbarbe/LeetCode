class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for x,y,r in queries:
            cur = 0
            for xi, yi in points:
                if dist((x, y), (xi, yi)) <= r:
                    cur += 1
            res.append(cur)
        return res