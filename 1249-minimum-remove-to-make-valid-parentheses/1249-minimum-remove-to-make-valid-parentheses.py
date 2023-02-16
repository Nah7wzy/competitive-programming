class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #count number of opening and closing brackets to remove first
        cl = set()
        stack = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append('(')
            if char == ')':
                if not stack:
                    cl.add(i)
                else:
                    stack.pop()
        op = len(stack)
        
        res = ""
        for j in range(len(s) - 1, -1, -1):
            if j not in cl:
                if s[j] == '(' and op > 0:
                    op -= 1
                    continue
                else:
                    res = s[j] + res
                    
        return res