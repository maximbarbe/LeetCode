class Solution:
    def binaryGap(self, n: int) -> int:
        rep = bin(n)[2:]
        indices = []
        m = 0
        for i in range(len(rep)):
            if rep[i] == '1':
                indices.append(i)
        for i in range(len(indices) - 1):
            m = max(m, indices[i + 1] - indices[i])
        return m