class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[j for _ in range(len(word1) + 1)] for j in range(len(word2), 0, -1)]
        dp.append([i for i in range(len(word1), -1, -1)])
        
        for i in range(len(word2) - 1, -1, -1):
            for j in range(len(word1) -1, -1, -1):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        return dp[0][0]
        
        