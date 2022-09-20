class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid[0]), len(grid)
        inbound = lambda x, y : 0 <= x < n and 0 <= y < m
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def dfs(i, j):
            if not inbound(i, j) or grid[i][j] == '0':
                return 
            grid[i][j] = '0'
            for x, y in directions:
                dfs(i+x, y+j)
        res = 0        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
                    
        return res