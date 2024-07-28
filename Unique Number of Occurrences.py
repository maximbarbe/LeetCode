class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c =Counter(arr)
        seen =dict()
        for val in c.values():
            if seen.get(val, False) == True:
                return False
            else:
                seen[val] = True
        return True