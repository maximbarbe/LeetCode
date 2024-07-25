class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum = inf
        res = []
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) < minimum:
                minimum = abs(arr[i + 1] - arr[i])
                res = [[arr[i], arr[i + 1]]]
            elif abs(arr[i + 1] - arr[i]) == minimum:
                res.append([arr[i], arr[i + 1]])
        return res