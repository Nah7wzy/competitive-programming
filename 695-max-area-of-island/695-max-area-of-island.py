class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        inbound = lambda i, j : 0 <= i < m and 0 <= j < n
        
        def dfs(i, j):
            if not inbound(i, j) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                res = dfs(i, j)
                max_area = max(res, max_area)
                
        return max_area