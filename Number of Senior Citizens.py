class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for text in details:
            if int(text[11:13]) > 60:
                res += 1
        return res