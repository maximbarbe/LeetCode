class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return len(max(sentences, key=lambda el:len(el.split(" "))).split(" "))