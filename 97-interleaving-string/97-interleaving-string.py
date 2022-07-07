class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):    return False
        x = False
        @cache
        def dp(i, j):
            nonlocal x
            if i == n and j == m:
                x = True
                return
            
            if i < n and s3[i+j] == s1[i]:
                dp(i+1, j)
            if j < m and s3[i+j] == s2[j]:
                dp(i, j+1)
        
        dp(0,0)
        return x