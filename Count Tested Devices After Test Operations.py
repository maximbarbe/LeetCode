class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        decrease = 0
        res = 0
        b = batteryPercentages
        for i in range(len(b)):
            if b[i] - decrease > 0:
                res += 1
                decrease += 1
        return res