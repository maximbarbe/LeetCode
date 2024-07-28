class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        matrix = [[inf for i in range(26)] for j in range(26)]
        for i in range(26):
            matrix[i][i] = 0
        for i in range(len(original)):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            matrix[u][v] = min(matrix[u][v], cost[i])
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        cost = 0
        for i in range(len(source)):
            u = ord(source[i]) - ord('a')
            v = ord(target[i]) - ord('a')
            cost += matrix[u][v]
        return -1 if cost == inf else cost