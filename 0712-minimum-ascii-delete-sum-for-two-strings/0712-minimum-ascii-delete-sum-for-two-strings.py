class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def dp(i, j):
            if i >= len(s1) or j >= len(s2):
                total_left = 0
                while i < len(s1):
                    total_left += ord(s1[i])
                    i += 1
                while j < len(s2):
                    total_left += ord(s2[j])
                    j += 1
                return total_left
            
            if s1[i] == s2[j]:
                return dp(i+1, j+1)
            else:
                return min(ord(s1[i]) + dp(i+1, j), ord(s2[j]) + dp(i, j+1))
        return dp(0,0)