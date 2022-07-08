class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        inbound = lambda r, c : (0 <= r < n) and (0 <= c < m)
        
        def dfs(r, c):
            if not inbound(r, c) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0 #to not revisit
            return (1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1))
        
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))
                
        return res