class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        if len(s)<2:
            return len(s)
        
        left, right, maxl = 0, 0, 0
        
        while right<len(s):
            if s[right] not in window:
                window.add(s[right])
                maxl = max(maxl, len(window))
            else:
                while s[left] != s[right]:
                    window.remove(s[left])
                    left+=1
                    
                window.remove(s[left])
                left+=1
                continue
            right+=1
        
        return maxl