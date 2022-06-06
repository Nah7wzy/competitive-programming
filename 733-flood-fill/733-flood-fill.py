class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m
        
        visited = set() 
        directions =[(0,1), (1,0), (-1,0), (0,-1)]
        color = image[sr][sc]
        
        def dfs(row, col):
            visited.add((row, col))
            image[row][col] = newColor
            for x, y in directions:
                nr, nc = row+x, col+y
                if inbound(nr, nc) and (nr, nc) not in visited and image[nr][nc] == color:
                    dfs(nr, nc)
                
        dfs(sr, sc)
        return image