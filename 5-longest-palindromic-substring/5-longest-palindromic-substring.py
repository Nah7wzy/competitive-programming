class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""    #calculate stretch of palindrome left and right for each letter
        length = 0
        
        def palindrome(l, r): #updates res (palindrome width for current letter)
            nonlocal res, length                            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length: #if longer palindrom
                    res = s[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1
            return
        
        # for odd length stretch from same index
        # for even length stretch from 2 adjacent index
        for i in range(len(s)):
            palindrome(i,i) #odd
            palindrome(i, i+1) #even
            
        return res
        
            