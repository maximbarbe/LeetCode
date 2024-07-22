class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda el:(el[0], el[1]))
        stack = []
        for start, end in intervals:
            if stack == [] or start > stack[-1][1]:
                stack.append([start, end])
            else:
                el = stack.pop()
                stack.append([min(start, el[0]), max(el[1], end)])
        return stack