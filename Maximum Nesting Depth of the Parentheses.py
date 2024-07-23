class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append("(")
            elif char == ")":
                stack.pop()
            if len(stack) > max_depth:
                max_depth += 1
        return max_depth