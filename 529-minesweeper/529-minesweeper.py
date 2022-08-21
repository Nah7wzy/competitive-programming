class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        inbound = lambda i, j: 0 <= i < len(board) and 0 <= j < len(board[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        
        def countMines(i, j):
            count = 0
            for x, y in directions:
                new_i, new_j = i + x, j + y
                if inbound(new_i, new_j):
                    count += 1 if board[new_i][new_j] == 'M' else 0
            return count
        
        def dfs(i, j):
            if inbound(i, j):
                cell = board[i][j]
                if cell == 'M':
                    board[i][j] = 'X'
                    return 
                if cell == 'E':
                    count = countMines(i, j)
                    if count:
                        board[i][j] = str(count)
                    else:
                        board[i][j] = 'B'
                        for x, y in directions:
                            dfs(i + x, j + y)
                            
        dfs(click[0], click[1])
        return board
                            
       