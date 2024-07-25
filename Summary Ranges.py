class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        piles = []
        prev = None
        for v in nums:
            if piles == [] or prev == None:
                piles.append([v])
                prev = v
            else:
                if v == prev + 1:
                    piles[-1].append(v)
                    prev = v
                else:
                    piles.append([v])
                    prev = v
        res = []
        for pile in piles:
            if len(pile) == 1:
                res.append(str(pile[0]))
            else:
                res.append(f"{pile[0]}->{pile[-1]}")
        return res