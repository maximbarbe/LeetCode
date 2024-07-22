class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for op in operations:
            if op.startswith("--") or op.endswith("--"):
                res -= 1
            else:
                res += 1
        return res