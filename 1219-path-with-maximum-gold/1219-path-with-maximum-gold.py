class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        inbound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        res = 0
        def backtrack(i, j, total):
            nonlocal res
            visited.add((i, j))
            total += grid[i][j]
            res = max(res, total)
            
            for x, y in directions:
                new_x, new_y = i + x, j + y
                if inbound(new_x, new_y) and grid[new_x][new_y] and (new_x, new_y) not in visited:
                    backtrack(new_x, new_y, total)
                    
            total -= grid[i][j]
            visited.remove((i, j))
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                backtrack(i, j, 0)
            
        return res
            
            