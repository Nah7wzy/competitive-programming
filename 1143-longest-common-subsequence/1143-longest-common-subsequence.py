class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range( m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[j] == text2[i]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        print(dp)        
        return dp[0][0]