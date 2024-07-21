class Solution:
    def frequencySort(self, s: str) -> str:
        s = [char for char in s]
        freq = defaultdict(lambda:0)
        for char in s:
            freq[char] += 1
        s.sort(key=lambda el:(freq[el], el), reverse=True)
        return "".join(s)