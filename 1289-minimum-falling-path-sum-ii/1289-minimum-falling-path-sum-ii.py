class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = m = len(grid)
        if n == 1: return grid[0][0]
        stack = [0 for i in range(n)]
        
        while n > 0:
            for i in range(m):
                grid[n-1][i] += stack[i]
            
            stack = [] 
            temp = nsmallest(2, grid[n-1])
            for x in range(m):
                if grid[n-1][x] == temp[0]:
                    stack.append(temp[1])
                else:
                    stack.append(temp[0])
                  
            n -= 1
        
        return min(grid[0])