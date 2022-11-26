class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap, [grid[0][0], (0,0)])
        
        def isValid(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i,j) not in visited
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)] 
        res = 0
        visited = set()
        while heap:
            curr = heapq.heappop(heap)
            res = max(res, curr[0])
            visited.add(curr[1])
            
            if (curr[1][0], curr[1][1]) == (len(grid) - 1, len(grid[0]) - 1):
                break
            
            for x,y in directions:
                new_x, new_y = x + curr[1][0], y + curr[1][1]
                if isValid(new_x, new_y) and (new_x, new_y) not in visited:
                    heapq.heappush(heap, [grid[new_x][new_y], (new_x, new_y)])
                    
        return res