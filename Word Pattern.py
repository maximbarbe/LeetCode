class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=  s.split(" ")
        if len(s) != len(pattern):
            return False
        inverse = dict()
        mapping = dict()
        for i in range(len(s)):
            if inverse.get(s[i], None) == None:
                inverse[s[i]] = pattern[i]
            else:
                if inverse[s[i]] != pattern[i]:
                    return False
            if mapping.get(pattern[i], s[i]) == s[i]:
                mapping[pattern[i]] = s[i]
            else:
                return False
        return True