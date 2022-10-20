class RandomizedSet:

    def __init__(self):
        self.stack = []
        self.d = {}
        self.elems = set()

    def insert(self, val: int) -> bool:
        if val in self.elems:
            return False
        else:
            self.elems.add(val)
            self.stack.append(val)
            self.d[val] = len(self.stack) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.elems:
            self.elems.remove(val)
            temp_ind, temp_val = self.d[val], self.stack[-1]
            self.stack[-1], self.stack[self.d[val]] = self.stack[self.d[val]], self.stack[-1]
            self.d[temp_val] = temp_ind
            self.stack.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.stack)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()