class Solution:
    def validPalindrome(self, s: str) -> bool:
        available = 1
        l, r = 0, len(s) - 1
        
        def check(i, j):
            nonlocal available
            if i >= j:
                return True
            if s[i] != s[j]:
                if available == 0:
                    return False
                else:
                    available -= 1
                    return check(i + 1, j) or check(i, j - 1)
            else:
                return check(i + 1, j - 1)
        
        return check(l, r)
