class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]
        for i in range(len(prices)):
            res = max(res, prices[i] - low)
            if prices[i] < low:
                low = prices[i]
                
        return res
    
    #just traverse looking for max and if its not max but lower than our current min, update the min and look in the rest for max