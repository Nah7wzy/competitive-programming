class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        def move(i, j):
            if i == m - 1 or j == n - 1:
                return 1 #only either going left or down possible which gives 1 possibility
            if dp[i][j] != -1:
                return dp[i][j] #return from memo
            
            dp[i][j] = move(i + 1, j) + move(i, j + 1)
            return dp[i][j]
        
        return move(0, 0)