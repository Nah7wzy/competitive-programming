class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        inbound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def dfs(i, j):
            perimeter = 0
            if (i,j) not in visited:
                if not inbound(i,j) or grid[i][j] == 0:
                    return 1
                visited.add((i,j))
                for x, y in directions:
                    perimeter += dfs(i+x, j+y)
               
            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr = dfs(i,j)
                    return curr
