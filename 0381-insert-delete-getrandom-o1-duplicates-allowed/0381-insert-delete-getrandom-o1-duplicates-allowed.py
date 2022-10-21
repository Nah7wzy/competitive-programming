class RandomizedCollection:

    def __init__(self):
        self.stack = []
        self.d = defaultdict(set)
        self.elems = set()
        self.freq = defaultdict(int)

    def insert(self, val: int) -> bool:
        self.stack.append(val)
        self.d[val].add(len(self.stack) - 1)
        self.freq[val] += 1
        if val in self.elems:
            return False
        else:
            self.elems.add(val)
            return True


    def remove(self, val: int) -> bool:
        if val in self.elems:
            self.freq[val] -= 1
            if self.freq[val] == 0:
                self.elems.remove(val)

            remove, last = self.d[val].pop(), self.stack[-1]
            self.stack[remove] = last
            self.d[last].add(remove)
            self.d[last].remove(len(self.stack) - 1)
            
            self.stack.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.stack)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()