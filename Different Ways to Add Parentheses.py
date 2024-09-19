class Solution:

    @lru_cache
    def dfs(self, expr):
        if expr.isnumeric():
            return [int(expr)]
        else:
            res = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    lhs = self.dfs(expr[:i])
                    rhs = self.dfs(expr[i+1:])
                    for v1 in lhs:
                        for v2 in rhs:
                            res.append(eval(f"{v1}{char}{v2}"))
            return res

    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.dfs(expression)