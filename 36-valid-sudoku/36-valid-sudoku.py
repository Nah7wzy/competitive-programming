class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def subbox(i, j):
            return ( (j // 3 + 1) + ((i // 3) * 3) )
            
        digits = defaultdict(set) #keep the boxes where digits appear and if they appear in the same box again return false
        for i in range(9):
            row, col = set(), set()
            for j in range(9):
                if (board[i][j] != '.' and (board[i][j] in row or subbox(i,j) in digits[board[i][j]])) or (board[j][i] != '.' and board[j][i] in col):
                    return False
                digits[board[i][j]].add(subbox(i,j))
                row.add(board[i][j])
                col.add(board[j][i])             
                
        return True
        