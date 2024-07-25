class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [i for i in range(1, n+1)]
        return "".join(map(str, list(itertools.permutations(numbers))[k-1]))