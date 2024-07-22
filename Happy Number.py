class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = sum(map(lambda el:int(el) ** 2, [char for char in str(n)]))
            