class Solution:
    def minChanges(self, n: int, k: int) -> int:
        
        n = bin(n)[2:]
        k = bin(k)[2:]
        if len(n) > len(k):
            k = k.zfill(len(n))
        elif len(k) > len(n):
            n = n.zfill(len(k))
        res = 0
        for i in range(len(n)):
            if n[i] == "0":
                if k[i] == "1":
                    return -1
            else:
                if k[i] == '0':
                    res += 1
        return res