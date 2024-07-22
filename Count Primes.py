class Solution:
    def countPrimes(self, n: int) -> int:
        if n in [0, 1]:
            return 0
        primes = [True] * (n)
        primes[0] = False
        primes[1] = False
        for i in range(2, n):
            if primes[i] == True:
                temp = i
                while temp + i < n:
                    temp += i
                    primes[temp] = False
        res = 0
        for i in range(len(primes)):
            if primes[i]:
                res += 1
        return res