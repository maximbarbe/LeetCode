class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessthan = 0
        equal = 0
        morethan = 0
        for i in range(len(nums)):
            if nums[i] < pivot:
                lessthan += 1
            elif nums[i] == pivot:
                equal += 1
            else:
                morethan += 1
        l_idx = 0
        e_idx = 0
        m_idx = 0
        res = [None] * (len(nums))
        for i in range(len(nums)):
            if nums[i] < pivot:
                res[l_idx]=nums[i]
                l_idx += 1
            elif nums[i] == pivot:
                res[lessthan + e_idx] = nums[i]
                e_idx += 1
            else:
                res[lessthan + equal + m_idx] = nums[i]
                m_idx += 1
        return res