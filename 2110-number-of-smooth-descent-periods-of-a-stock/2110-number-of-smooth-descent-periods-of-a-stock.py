class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]
        count = 0
        for i in range(1, n+1):
            dp.append(i + dp[-1]) #array of possible combination for x length valid subarray (math)
            
        i, j = 0, 1
        while  j < n:
            curr = 1 #keep len of valid
            while j < n and prices[j-1] - prices[j] == 1:
                curr += 1
                j += 1
            
            if curr != 1:
                count += dp[curr] - curr #add possible combinations for the found length of subarray
                
            i = j
            j += 1
            
        return count + n