class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                for x in temp:
                    stack.append(x)
            else:
                stack.append(i)
                
        return ''.join(stack)