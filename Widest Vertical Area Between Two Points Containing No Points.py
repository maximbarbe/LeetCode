class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda el:el[0])
        res = 0
        for i in range(len(points) - 1):
            if points[i + 1][0] - points[i][0] > res:
                res = points[i + 1][0] - points[i][0]
        return res