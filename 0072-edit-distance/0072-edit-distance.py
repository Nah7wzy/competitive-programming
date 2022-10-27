class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #use i, j index as state for the dp and try out the three options
        #insert move j only, delete move i only, replace move both - add 1 for all three; match move both without adding
        memo = {}
        def dp(i, j):
            if i >= len(word1): #need to insert remaining
                return len(word2) - j
            if j >= len(word2): #need to delete remaining
                return len(word1) - i
            if i >= len(word1) and j >= len(word2): 
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                return dp(i+1, j+1)
            
            operations = 1
            operations += min(dp(i, j+1), dp(i+1, j), dp(i+1, j+1))
            memo[(i,j)] = operations
            
            return memo[(i,j)]
        
        return dp(0, 0)
        