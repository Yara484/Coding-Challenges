class MyHashMap:

    def __init__(self):
        self.newMap = []

    def put(self, key: int, value: int) -> None:
        for i, (curr_key, curr_value) in enumerate(self.newMap):
            if curr_key == key:
                self.newMap[i][1] = value  
                return  
        self.newMap.append([key, value])

    def get(self, key: int) -> int:
        for curr_key, curr_value in self.newMap:
            if curr_key == key:
                return curr_value
        return -1    

    def remove(self, key: int) -> None:
        for i, (curr_key, curr_value) in enumerate(self.newMap):
            if curr_key == key:
                self.newMap.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)