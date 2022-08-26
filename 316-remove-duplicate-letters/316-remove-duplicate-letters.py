class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        unique = {}
        for i in range(len(s)): #keep track of greatest indexes of each unique element
            unique[s[i]] = i
            
        stack = [] #monotonic stack and remove when finding smaller only if it can appear later (using the dictionary index)
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                while stack and stack[-1] > s[i] and unique[stack[-1]] > i:
                    seen.remove(stack.pop())
                stack.append(s[i])
                
        return ''.join(stack)
                
        
            
                