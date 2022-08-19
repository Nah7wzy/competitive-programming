class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        inbound = lambda i, j : 0 <= i < m and 0 <= j < n
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def dfs(i, j):
            if inbound(i, j) and grid[i][j] == 1:
                grid[i][j] = 0
                for x, y in directions:
                    dfs(i + x, j + y)
        
        for a in range(m):
            for b in range(n):
                if a == 0 or b == 0 or a == m - 1 or b == n - 1:
                    dfs(a, b)
        count = 0           
        for a in range(m):
            for b in range(n):
                count += 1 if grid[a][b] == 1 else 0
                
        return count