class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        res = 0
        for key in c1.keys():
            if c1[key] == 1 and c2[key] == 1:
                res += 1
        return res