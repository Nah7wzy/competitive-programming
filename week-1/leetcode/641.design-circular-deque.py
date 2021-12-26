from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.k=k
        self.arr=deque(maxlen=k)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False 
        self.arr.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False 
        self.arr.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False 
        self.arr.pop()
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.arr[0]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.arr[-1]

    def isEmpty(self) -> bool:
        return len(self.arr)==0

    def isFull(self) -> bool:
        return self.k==len(self.arr)