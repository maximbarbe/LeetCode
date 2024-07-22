class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = dict()
        res = set()
        if len(s) <= 10:
            return []
        for i in range(0, len(s) - 9):
            cur = s[i:i + 10]
            if seen.get(cur, False) == False:
                seen[cur] = True
            else:
                res.add(cur)
        return list(res)