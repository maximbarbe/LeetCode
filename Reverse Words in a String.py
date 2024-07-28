class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        cur = ""
        for i in range(len(s)):
            if s[i] == " ":
                if cur != "":
                    words.append(cur)
                    cur = ""
            else:
                cur += s[i]
        else:
            if cur != "":
                words.append(cur)
        return " ".join(words[::-1])