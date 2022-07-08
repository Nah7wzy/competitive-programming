class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(x1, y1, x2, y2, x3, y3):
            return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) * (1/2)
        
        n = len(points)
        res = 0
        for i in range(n - 2):
            x1, y1 = points[i]
            for j in range(i + 1, n - 1):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    res = max(res, area(x1, y1, x2, y2, x3, y3))
        
        return res