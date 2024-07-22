class MyHashMap:

    def __init__(self):
        self.hashmap = [None] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        return self.hashmap[key] if self.hashmap[key] != None else -1

    def remove(self, key: int) -> None:
        self.hashmap[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)