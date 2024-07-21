class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for key in c1:
            if c1[key] > c2[key]:
                return False
        else:
            return True