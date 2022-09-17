class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        inbound = lambda i, j : 0 <= i < m and 0 <= j < n
        
        freshcount = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    freshcount += 1
         
        time = 0
        while q:
            count = len(q)
            for _ in range(count):
                orange = q.popleft()
                for x, y in directions:
                    new_x, new_y = orange[0] + x, orange[1] + y
                    if inbound(new_x, new_y) and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        freshcount -= 1
                        q.append((new_x, new_y))
                        
            if q:
                time += 1
                
        return time if freshcount == 0 else -1
                                 
                    