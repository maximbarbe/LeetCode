class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)
        for key, val in c2.items():
            if val > c1[key]:
                return key