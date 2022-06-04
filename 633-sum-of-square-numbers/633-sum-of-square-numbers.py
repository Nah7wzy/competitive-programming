class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = sqrt(c)
        l, r = 0, floor(x)
        
        while l <= r:
            if l*l + r*r == c:
                return True
            elif l*l + r*r > c:
                r -= 1
            else:
                l += 1
                
        return False