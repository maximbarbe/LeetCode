class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = defaultdict(lambda:[])
        cities = set()
        for src, dest in paths:
            cities.add(src)
            cities.add(dest)
            outgoing[src].append(dest)
        for c in cities:
            if len(outgoing[c]) == 0:
                return c