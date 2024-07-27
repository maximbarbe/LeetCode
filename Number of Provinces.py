class Solution:

    def bfs(self, idx, visited, isConnected):

        q = deque([idx])
        visited[idx] = True
        while len(q) != 0:
            cur = q.popleft()
            for i in range(len(isConnected)):
                if isConnected[cur][i] == 1 and visited[i] == False:
                    visited[i] = True
                    q.append(i)


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = [False] * len(isConnected)
        for i in range(len(isConnected)):
            if visited[i] == False:
                res += 1
                self.bfs(i, visited, isConnected)
        return res