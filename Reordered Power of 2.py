class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = [char for char in str(n)]
        for perm in itertools.permutations(digits):
            if perm[0] == "0":
                continue
            num = int("".join(perm))
            if floor(log2(num)) == log2(num):
                return True
        else:
            return False