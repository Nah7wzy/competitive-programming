class Solution:
    def calc(self,a,b,c):
        if c == '/':
            if a < 0 and b > 0 or a > 0 and b < 0:
                return -(abs(b)//abs(a))
            if abs(b) < abs(a):
                return 0
            else:
                return b//a
        return b+a if c == '+' else b-a if c == '-' else b*a if c == '*' else b//a
    def evalRPN(self, tokens: List[str]) -> int:
        exp=[]
        op=['+','-','*','/']
        for i in tokens:
            if i in op:
                a=exp.pop()
                b=exp.pop()
                c=self.calc(int(a),int(b),i)
                exp.append(c)
            else:
                exp.append(i)
        return exp[0]
