class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free = 0
        buy = cool = float('-inf')
        for p in prices:
            free, buy, cool = max(free, cool), max(buy, free - p), buy + p
            
        return max(free, cool)