class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        target = dict()
        for i in range(len(arr)):
            if target.get(arr[i], False) == False:
                target[arr[i] * 2] = True
                target[arr[i] / 2] = True
            else:
                return True
        return False