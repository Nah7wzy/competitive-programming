class Solution:
    def calc(self,a,b,c):
        return b+a if c=='+' else b-a if c=='+' else b*a if c=='*' else b//a
    def evalRPN(self, tokens) -> int:
        exp=[]
        op=['+','-','*','/']
        for i in tokens:
            if i in op:
                a=exp.pop()
                b=exp.pop()
                c=self.calc(int(a),int(b),i)
                print(c)
                exp.append(c)
            else:
                exp.append(i)
        return exp[0]

x=Solution()
print(x.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))