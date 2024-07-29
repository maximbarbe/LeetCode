class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.rstrip("/").split("/")
        stack = []
        for dir in dirs:
            if dir == "..":
                if len(stack) != 0:
                    stack.pop()
            elif dir == "." or dir == "":
                continue
            else:
                stack.append(dir)
        return "/" + "/".join(stack)