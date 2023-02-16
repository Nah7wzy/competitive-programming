class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(start, pre, last_count, left):
            if left < 0:
                return float("inf") 
            
            if start >= len(s):
                return 0
            
            if s[start]==pre:
                cost = 1 if last_count in (1,9,99) else 0 
                return cost + dp(start+1, pre, last_count+1, left) 
            else:
                keep = 1  + dp(start+1, s[start], 1, left) 
                delete = dp(start+1, pre, last_count, left-1) 
                return min(keep, delete)
            
        return dp(0,"", 0,k)