class Solution:

    def bfs(self, graph, colors, i):
        colors[i] = 0
        q = deque([i])
        while len(q) != 0:
            cur = q.popleft()
            for v in graph[cur]:
                if colors[v] == None:
                    colors[v] = colors[cur] ^ 1
                    q.append(v)
                else:
                    if colors[v] == colors[cur]:
                        return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [None for i in range(len(graph))]
        bipartite = True
        for i in range(len(graph)):
            if colors[i] == None:
                bipartite = bipartite and self.bfs(graph, colors, i)
        return bipartite
