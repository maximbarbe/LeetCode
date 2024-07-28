class Solution:

    def permutations(self, s, length, idx, cur, res):
        if idx == length:
            res.append(cur)
            return
        else:
            if s[idx].isdigit():
                self.permutations(s, length, idx + 1, cur + s[idx], res)
            else:
                self.permutations(s, length, idx + 1, cur + s[idx].lower(), res)
                self.permutations(s, length, idx + 1, cur + s[idx].upper(), res)
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        self.permutations(s, len(s), 0, "", res)
        return res
        