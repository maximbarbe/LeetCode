class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nums = list(map(lambda el: [char for char in str(el)], nums))
        res = []
        for i in range(len(nums)):
            cur = []
            for j in range(len(nums[i])):
                cur.append(mapping[int(nums[i][j])])
            res.append((int("".join(map(str, cur))), int("".join(nums[i]))))
        res.sort(key=lambda el:el[0])
        return [res[i][1] for i in range(len(res))]