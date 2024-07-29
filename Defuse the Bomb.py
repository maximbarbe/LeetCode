class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            res = [0] * len(code)
            for i in range(len(code)):
                cur = 0
                for j in range(1, k+1):
                    cur += code[(i + j)%len(code)]
                res[i] = cur
            return res
        else:
            res = [0] * len(code)
            for i in range(len(code)):
                cur = 0
                for j in range(1, abs(k) + 1):
                    cur += code[(i - j)%len(code)]
                res[i] = cur
            return res