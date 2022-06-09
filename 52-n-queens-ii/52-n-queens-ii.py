class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        posdiag, negdiag, col = set(), set(), set()
        
        def place(i):
            nonlocal count
            if i == n:
                count += 1
                return 
            
            for j in range(n):
                if j not in col and i+j not in posdiag and j-i not in negdiag:
                    
                    posdiag.add(i+j);   negdiag.add(j-i);   col.add(j)
                    place(i+1)
                    posdiag.remove(i+j);    negdiag.remove(j-i);    col.remove(j)
                    
        place(0)
        return count