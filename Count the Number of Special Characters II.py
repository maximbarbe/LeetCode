class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        positions = defaultdict(lambda:[])
        for i, char in enumerate(word):
            positions[char].append(i)
        res = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            if len(positions[c]) != 0 and len(positions[c.upper()]) != 0 and positions[c][-1] < positions[c.upper()][0]:
                res += 1
        return res