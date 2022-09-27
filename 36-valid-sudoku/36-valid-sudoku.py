class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        for i in range(9):
            digits = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in digits:
                    return False
                digits.add(board[i][j])
        #column check
        for j in range(9):
            digits = set()
            for i in range(9):
                if board[i][j] != '.' and board[i][j] in digits:
                    return False
                digits.add(board[i][j])
                
        #sub-box check
        x = y = 0
        while x < 9:
            digits = set()
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] != '.' and board[i][j] in digits:
                        return False
                    digits.add(board[i][j])
            y += 3
            if y >= 9:
                y = 0
                x += 3
        return True
        