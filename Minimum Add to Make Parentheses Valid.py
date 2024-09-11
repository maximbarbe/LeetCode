class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if not stack or char == "(":
                stack.append(char)
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(char)

        return len(stack)