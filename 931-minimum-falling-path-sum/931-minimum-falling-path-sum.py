class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = m = len(matrix)
        if n == 1: return matrix[0][0]
        stack = [0 for i in range(n)]
        
        while n > 0:
            for i in range(m):
                matrix[n-1][i] += stack[i]
            
            stack = [] 
            for x in range(m):
                if x == 0:
                    stack.append(min(matrix[n-1][0], matrix[n-1][1]))
                elif x == m - 1:
                    stack.append(min(matrix[n-1][x], matrix[n-1][x-1]))
                else:
                    stack.append(min(matrix[n-1][x-1], matrix[n-1][x], matrix[n-1][x+1]))
                  
            n -= 1
        
        return min(matrix[0])