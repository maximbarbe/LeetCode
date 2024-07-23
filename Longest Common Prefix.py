class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda el:len(el),reverse=True)
        cur = [char for char in strs[0]]
        for word in strs:
            pref = []
            for i, char in enumerate(word):
                if i >= len(cur):
                    break
                if cur[i] == char:
                    pref.append(char)
                else:
                    break
            cur = pref
        return "".join(cur)