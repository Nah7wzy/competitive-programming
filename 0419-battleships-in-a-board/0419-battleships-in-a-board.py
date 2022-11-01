class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:   
        m, n = len(board[0]), len(board)
        parent, rank = {}, {}
        for r in range(n): #initialize parent to itself and rank to 1 or 0
            for c in range(m):
                parent[(r,c)] = (r,c) 
                rank[(r,c)] = 1 if board[r][c] == 'X' else 0
                
        def find(node):
            if node == parent[node]:
                return parent[node]

            parent[node] = find(parent[node])
            return parent[node]

        def unite(a, b):
            pa = find(a)
            pb = find(b)

            if pa != pb:
                if rank[pa] >= rank[pb]:
                    parent[pb] = pa
                    rank[pa] += rank[pb]
                    rank[pb] = 0
                else:
                    parent[pa] = pb
                    rank[pb] += rank[pa]
                    rank[pa] = 0
                    
        inbound = lambda x, y : 0 <= x < n and 0 <= y < m         
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'X':
                    down, right = (r+1, c), (r, c+1)
                    if inbound(down[0], down[1]) and board[down[0]][down[1]] == 'X':
                        unite((r,c), down)
                    if inbound(right[0], right[1]) and board[right[0]][right[1]] == 'X':
                        unite((r,c), right)
        res = 0               
        for val in rank.values():
            res += 1 if val else 0
            
        return res
                
                    
        