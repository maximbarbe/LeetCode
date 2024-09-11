class Solution:
    def minimumPushes(self, word: str) -> int:
        keys = [0]*8
        idx = 0
        c = Counter(word)
        res = 0
        for val in sorted(c.values(), reverse=True):
            keys[idx] += 1
            res += val * keys[idx]
            idx = (idx + 1)%8
        return res