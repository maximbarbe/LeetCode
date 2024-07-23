class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        smaller = []
        bigger = deque()
        for i in range(1, ceil(sqrt(n))):
            if n % i == 0:
                smaller.append(i)
                bigger.appendleft(n//i)
        if ceil(sqrt(n))**2 == n:
            smaller.append(ceil(sqrt(n)))
        if len(smaller) + len(bigger) < k:
            return -1
        else:
            if k <= len(smaller):
                return smaller[k - 1]
            else:
                return bigger[k - len(smaller) - 1]