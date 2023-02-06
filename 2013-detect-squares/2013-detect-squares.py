class DetectSquares:

    def __init__(self):
        self.counter = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        self.counter[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in list(self.counter):
            if (abs(x - px) == abs(y - py)) and x != px and y != py:
                ans = self.counter[(x, y)] * self.counter[(x, py)] * self.counter[(px, y)]
               
                res += ans
        return res
        
        

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)