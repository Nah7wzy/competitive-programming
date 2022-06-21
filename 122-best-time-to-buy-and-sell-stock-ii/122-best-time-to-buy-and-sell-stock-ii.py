class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        #buy and sell when ever an increase at each step..holding on to a stock (jumping) is same as advancing daily
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
                        
        return profit
            