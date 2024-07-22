class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = [(names[i], i) for i in range(len(names))]
        temp = sorted(temp, key=lambda el:heights[el[1]], reverse=True)
        return [temp[i][0] for i in range(len(temp))]