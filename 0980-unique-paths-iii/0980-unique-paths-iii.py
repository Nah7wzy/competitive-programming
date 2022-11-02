class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        inbound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        visited = set()
        def backtrack(i, j, no_of_paths):
            if grid[i][j] == 2:
                return 1 if len(visited) == no_of_paths else 0
            
            res = 0
            for x, y in directions:
                nx, ny = x+i, y+j
                if inbound(nx, ny) and (nx, ny) not in visited and grid[nx][ny] >= 0:
                    visited.add((nx, ny))
                    res += backtrack(nx, ny, no_of_paths)
                    visited.remove((nx, ny))
                    
            return res
        
        paths = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                paths += 1 if grid[i][j] == 0 else 0
                if grid[i][j] == 1:
                    start = (i, j)
                    visited.add(start)
                    
        # print(paths, start)        
        return backtrack(start[0], start[1], paths)
                