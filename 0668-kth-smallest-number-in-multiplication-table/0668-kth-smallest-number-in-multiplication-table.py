class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def count(x):
            total = 0
            for i in range(1, m + 1): #for each column count how many lesser numbers
                total += min(n, x // i) #n is the boundary since u cant count more than n nums in a column
                #num // i bc the jump is i for ith column
            return total
        
        l, r = 1, m * n
        while l <= r:
            mid = (l+r)//2
            if count(mid) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l