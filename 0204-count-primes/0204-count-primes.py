class Solution:
    def countPrimes(self, n: int) -> int:
        #0 - prime, -1 - composite
        d = [0 for _ in range(n)]
        count = 0
        
        for i in range(2, n):
            if d[i] == 0:
                count += 1
                if i > (n ** 0.5):  continue
                multiplier = i ** 2
                while multiplier < n:
                    d[multiplier] = -1
                    multiplier += i
                    
        return count
        