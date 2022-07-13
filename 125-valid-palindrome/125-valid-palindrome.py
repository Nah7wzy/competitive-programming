class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            word += i.lower() if i.isalpha() or i.isdigit() else ""
        
        l, r = 0, len(word) - 1
        while l <= r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
            
        return True