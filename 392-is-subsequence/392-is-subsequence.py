class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        f = n = 0
        while f < len(s):
            while t and n < len(t) and s[f] != t[n]:
                n += 1
                if n >= len(t):
                    return False
            f += 1
            n += 1
        if s and t and f >= len(s) and n >= len(t) and s[-1] != t[-1]:
            return False
        return True if len(s) < len(t) else s == t