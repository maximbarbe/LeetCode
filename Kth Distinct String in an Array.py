class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        res = []
        for key in c.keys():
            if c[key] == 1:
                res.append(key)
        if k - 1 > len(res) - 1:
            return ""
        else:
            return res[k - 1]