class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        res = ""
        changed = middle = False
        for i in range(len(palindrome)-1):
            if palindrome[i] != "a" and not changed and not middle:
                if len(palindrome)%2 != 0 and i == len(palindrome) //2:
                    middle = True
                    res += palindrome[i]
                    continue
                res += "a"
                changed = True
            else:
                res += palindrome[i]
            
        if not changed or middle:
            res += "b"
        else:
            res += palindrome[i+1]
        return res