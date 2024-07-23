class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp  = [("".join(sorted(strs[i])), strs[i]) for i in range(len(strs))]
        groups = defaultdict(lambda:[])
        for i in range(len(temp)):
            groups[temp[i][0]].append(temp[i][1])
        return list(groups.values())