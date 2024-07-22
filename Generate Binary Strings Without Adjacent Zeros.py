class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = ["0", "1"]
        for i in range(2, n+1):
            temp = res
            res = []
            for k in temp:
                if k[-1] == "1":
                    res.append(k + "0")
                res.append(k+"1")
        return res