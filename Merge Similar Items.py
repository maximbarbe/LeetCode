class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weights = defaultdict(lambda:0)
        for v, w in items1:
            weights[v] += w
        for v, w in items2:
            weights[v] += w
        return sorted([[key, val] for key, val in weights.items()], key=lambda el:el[0])