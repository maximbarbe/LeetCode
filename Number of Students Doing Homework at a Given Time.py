class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        times = [0] * (1001)
        for i in range(len(startTime)):
            for v in range(startTime[i], endTime[i] + 1):
                times[v] += 1
        return times[queryTime]