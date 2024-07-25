class Solution:
    def sortSentence(self, s: str) -> str:

        s = s.split(" ")
        s.sort(key=lambda el:int(el[-1]))
        return " ".join(map(lambda el:el[:-1], s))