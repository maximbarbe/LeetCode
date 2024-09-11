class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(map(lambda el: bin(int(el))[2:], date.split("-")))