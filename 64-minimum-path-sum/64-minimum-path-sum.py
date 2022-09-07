class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)       
        
        for i in range(n):
            for j in range(m):
                if i == 0:
                    grid[i][j] += grid[i][j-1] if j!= 0 else 0
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[-1][-1]
        