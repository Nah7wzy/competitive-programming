class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = str(self.fact(n))
        count = 0
        
        for i in range(len(res)-1, 0, -1):
            if res[i] == "0":
                count += 1
            else:
                return count
        return count
    
    def fact(self,n):
        if n <= 1:
            return n
        else:
            return n * self.fact(n-1)