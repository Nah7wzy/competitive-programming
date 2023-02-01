class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        answer = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(1, m):
                mat[i][j] += mat[i][j-1]
        
        for i in range(n):
            for j in range(m):
                r1 = 0 if i - k < 0 else i - k
                r2 = n - 1 if i + k >= n else i + k
                for r in range(r1, r2+1):
                    c1 = 0 if j - k < 0 else j - k
                    c2 = m - 1 if j + k >= m else j + k
                    
                    answer[i][j] += mat[r][c2] - (0 if c1 == 0 else mat[r][c1-1])
       
        return answer
                