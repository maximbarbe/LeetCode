class Solution:
    def isThree(self, n: int) -> bool:
        divisors = 0
        for i in range(2, n):
            if n % i == 0:
                divisors += 1
        return divisors == 1