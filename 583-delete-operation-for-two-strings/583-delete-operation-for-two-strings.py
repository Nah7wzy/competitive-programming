class Solution:
    def minDistance(self, word1: str, word2: str) -> int: 
        n, m = len(word1), len(word2)
        dp = [[0 for x in range(n + 1)] for y in range(m + 1)]
        
        for r in range(m+1):
            for c in range(n+1):
                if r == 0 or c == 0:
                    dp[r][c] = max(r, c)
                elif word1[c-1] == word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1])
        
        return dp[-1][-1]