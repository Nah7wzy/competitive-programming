class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 1
        curr = points[0][1]
        # print(points)
        for point in points:
            if point[0] > curr:
                res += 1
                curr = point[1]
            elif point[1] < curr:
                curr = point[1]
                
        return res