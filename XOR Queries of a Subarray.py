class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref =  [0] * (len(arr) + 1)
        for i in range(len(arr)):
            pref[i + 1] = arr[i] ^ pref[i]
        res = [0] * len(queries)
        for k, (i, j) in enumerate(queries):
            res[k] = pref[j + 1] ^ pref[i]
        return res