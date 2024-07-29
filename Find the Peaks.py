class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        arr= mountain
        for i in range(1, len(mountain) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                res.append(i)
        return res