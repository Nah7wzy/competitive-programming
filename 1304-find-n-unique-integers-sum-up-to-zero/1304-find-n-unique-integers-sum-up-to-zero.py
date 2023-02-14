class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        if not n%2 == 0:
            arr.append(0)
            for i in range(1, n//2 + 1):
                arr.append(i)
                arr.append(-i)
        else:
            for i in range(1, n//2 + 1):
                arr.append(i)
                arr.append(-i)
                
        return arr