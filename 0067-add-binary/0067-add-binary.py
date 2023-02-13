class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        b = ("0" * (len(a) - len(b))) + b

        q = deque()
        carry = 0
        for i in range(len(b)-1, -1, -1):
            x, y = int(a[i]), int(b[i])

            if x and y:
                if carry:
                    q.appendleft('1')
                else:
                    q.appendleft('0')
                carry = 1
            elif x or y:
                if carry:
                    q.appendleft('0')
                    carry = 1
                else:
                    q.appendleft('1')
            else:
                if carry:
                    q.appendleft('1')
                    carry = 0
                else:
                    q.appendleft('0')
        if carry:
            q.appendleft('1')
        
        return "".join(e for e in q)
