class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False] * (n)
        visited[source] = True
        q = deque([source])
        edge = [[] for i in range(n)]
        for u, v in edges:
            edge[u].append(v)
            edge[v].append(u)
        
        while len(q) != 0:
            cur = q.popleft()
            if cur == destination:
                return True
            for dest in edge[cur]:
                if visited[dest] == False:
                    q.append(dest)
                    visited[dest] = True
        return False