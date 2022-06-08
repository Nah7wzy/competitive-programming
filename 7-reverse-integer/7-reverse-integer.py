class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: return 0
        
        x = str(x)
        if x >= '0':
            res = int(x[::-1])
            return res if res <= 2**31-1 else 0
        else:
            sub = x[1::]
            temp = sub[::-1]
            if int(temp) >= 2**31-1:
                return 0
            else:
                return int('-' + temp)