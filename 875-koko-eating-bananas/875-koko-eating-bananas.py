class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hours_taken(pace):
            hours = 0
            for bananas in piles:
                if bananas >= pace and bananas % pace == 0:
                    hours += bananas // pace
                else:
                    hours += bananas // pace + 1
            
            return hours
        
        left, right = 1, max(piles)
        while left < right:
            k = (left + right) // 2
            if hours_taken(k) > h:
                left = k + 1
            else:
                right = k
                
        return left