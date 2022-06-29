class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        order = []
        for i in range(len(points)):
            heappush(order, (self.distance(points[i]), i, points[i]))
        
        closest = []
        for i in range(k):
            closest.append(heappop(order)[2])
        
        return closest
        
    def distance(self, points):
        return math.sqrt(math.pow(points[0], 2) + math.pow(points[1], 2))