class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        converted = []
        for v in timePoints:
            h, m = map(int, v.split(":"))
            converted.append(h*60 + m)
        converted.sort()
        res = inf
        for i in range(len(converted)):
            if (converted[(i + 1)%len(converted)] - converted[i])%1440 < res:
                res = (converted[(i + 1)%len(converted)] - converted[i])%1440
        return res