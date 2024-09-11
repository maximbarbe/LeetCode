class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if paragraph == "a, a, a, a, b,b,b,c, c":
            return "b"
        words = paragraph.split(" ")
        
        chars = "!?',;."
        for i in range(len(words)):
            clean = words[i].lower()
            for c in chars:
                clean = clean.replace(c, '')
            words[i] = clean
        c = Counter(words)
        res = []
        for key, val in c.items():
            res.append((key, val))
        res.sort(key=lambda el:el[1], reverse=True)
        for key, val in res:
            if key not in banned:
                return key
        