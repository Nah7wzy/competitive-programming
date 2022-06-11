class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        #turn the edges and anything connected to sth else then revert it at the end
        def dfs(i,j):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O': 
                board[i][j] = 'I'
                for x, y in directions:
                    dfs(i+x, j+y)
            else:
                return
            
        #call dfs on the edges
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board)-1, j)
            
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0])-1)
            
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] = "O" if board[x][y] == "I" else "X"
        