class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        for c in itertools.combinations(digits, 3):
            permutations = set([c[0] * 100 + c[1] * 10 + c[2], c[0] * 100 + c[2] * 10 + c[1], c[1] * 100 + c[0] * 10 + c[2], c[1] * 100 + c[2] * 10 + c[0], c[2] * 100 + c[0] * 10 + c[1], c[2] * 100 + c[1] * 10 + c[0]])
            for num in permutations:
                if num >= 100 and num % 2 == 0:
                    res.add(num)
        return sorted(res)