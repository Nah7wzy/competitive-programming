class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        res = [0 for x in range(n)]
        
        while n > 0:
            for x in range(n):
                triangle[n-1][x] += res[x]
                
            res = []  
            for i in range(n-1):
                res.append(min(triangle[n-1][i], triangle[n-1][i+1]))
                
            n -= 1
            
        return triangle[0][0]