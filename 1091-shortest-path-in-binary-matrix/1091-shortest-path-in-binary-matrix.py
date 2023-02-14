class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions =  [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]
        inbound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        q = deque([(0,0)])
        count = 0
        visited = set([(0,0)])
        
        
        while q:
            count += 1
            n = len(q)
            
            for _ in range(n):
                i, j = q.popleft()
                if (i, j) == (len(grid)-1, len(grid)-1):
                    return count
                
                for x, y in directions:
                    if (i + x, j + y) not in visited and inbound(i + x, j + y) and grid[i+x][j+y] == 0:
                        visited.add((i + x, j + y))
                        q.append((i + x, j + y))
                        
        return -1
                