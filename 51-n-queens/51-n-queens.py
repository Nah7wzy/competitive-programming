class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        board = [['.' for x in range(n)] for y in range(n)]
        posdiag, negdiag, col = set(), set(), set()
        
        def place(i):
            if i == n:
                results.append([''.join(row) for row in board])
                return 
            
            for j in range(n):
                if j not in col and i+j not in posdiag and j-i not in negdiag:
                    posdiag.add(i+j)
                    negdiag.add(j-i)
                    col.add(j)
                    board[j][i] = 'Q'
                    place(i+1)
                    posdiag.remove(i+j)
                    negdiag.remove(j-i)
                    col.remove(j)
                    board[j][i] = '.'
                    
        place(0)
        return results
                
                    
                