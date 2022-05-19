class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        
        for i in num:
            while stack and i < stack[-1] and k > 0:
                stack.pop()
                k-=1
            stack.append(i)
                                                 
        if k>0:
            while k!=0:
                stack.pop()
                k-=1
                
        s=''.join(stack)
                
        return str(int(s)) if s else "0"