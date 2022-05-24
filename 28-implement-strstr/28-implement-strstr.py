class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ptr1, ptr2 = 0, 0
        h, n = len(haystack), len(needle)
        ans = -1
        
        if n == 0:
            return 0
        if n > h:
            return -1
        
        while ptr1 < h:
            if needle[ptr2] == haystack[ptr1] and ptr2 < n-1:
                if ptr2 == 0:
                    ans = ptr1
                
                ptr2+=1
            elif needle[ptr2] == haystack[ptr1] and ptr2 == n-1:
                return ans if ans != -1 else ptr1
            elif needle[ptr2] != haystack[ptr1] and ptr2 > 0:
                ptr2 = 0
                ptr1 = ans 
                ans = -1
                
            ptr1 += 1
            
        return -1