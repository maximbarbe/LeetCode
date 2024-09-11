class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start, end = 0, len(s)
        res = []
        for char in s:
            match char:
                case 'I':
                    res.append(start)
                    start += 1
                case _:
                    res.append(end)
                    end -= 1
        res.append(start)
        return res
        