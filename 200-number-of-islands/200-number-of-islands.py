class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid[0]), len(grid)
        inbound = lambda x, y : 0 <= x < n and 0 <= y < m
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        parent = {}
        rank = {}
        for r in range(n): #initialize parent to itself and rank to 1 or 0
            for c in range(m):
                parent[(r,c)] = (r,c) 
                rank[(r,c)] = 1 if grid[r][c] == '1' else 0
                
        def find(i, j):
            if parent[(i,j)] == (i, j):
                return (i, j)
            parent[(i, j)] = find(parent[(i,j)][0], parent[(i,j)][1]) #track back parent and assign on return for each to avoid recomputation
            return parent[(i,j)]
        
        def union(a, b):
            a_par = find(a[0], a[1])
            b_par = find(b[0], b[1])
            
            if a_par != b_par: #if they have different parents they can be united
                if rank[a_par] < rank[b_par]:
                    parent[a_par] = b_par
                    rank[b_par] += rank[a_par]
                    rank[a_par] = 0
                else:
                    parent[b_par] = a_par
                    rank[a_par] += rank[b_par]
                    rank[b_par] = 0
        
        for r in range(n):
            for c in range(m):
                for x, y in directions:
                    new_r, new_c = r + x, c + y
                    if inbound(new_r, new_c) and grid[new_r][new_c] == '1' and grid[r][c] == '1':
                        union((new_r, new_c), (r, c))
        res = 0
        for val in rank.values(): #positive rank means its the representative parent
            res += 1 if val else 0
        return res