class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = dict()
        for char in allowed:
            allow[char] = True
        res = 0
        for word in words:
            for char in word:
                if allow.get(char, False) == False:
                    break
            else:
                res += 1
        return res