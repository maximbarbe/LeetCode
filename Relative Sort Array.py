class Solution:

    

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        indices = {}
        added = {}
        for i in range(len(arr2)):
            indices[arr2[i]] = i

        arr1.sort(key=lambda el:(indices.get(el, inf), el))
        return arr1
        