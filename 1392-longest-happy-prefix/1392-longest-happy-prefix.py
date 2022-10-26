class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        i, j = 0, 1
        while j < len(s):
            if s[i] == s[j]:
                lps[j] = i + 1
                i += 1
            else:
                if i == 0:                    
                    lps[j] = 0
                else:
                    i = lps[i-1]
                    continue
            j += 1
            
        return s[:lps[-1]]
                    