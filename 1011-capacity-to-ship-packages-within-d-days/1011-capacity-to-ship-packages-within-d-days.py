class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #use sum of weights as max possible capacity and max weight as minimum and binary search to find out the day result
        #function to return days for a chosen capacity
        def days_taken(cap):
            d = 1
            curr_weight = weights[0]
            for i in range(1, len(weights)):
                if curr_weight + weights[i] > cap:
                    d += 1
                    curr_weight = 0
                curr_weight += weights[i]
            return d
        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if days_taken(mid) > days:
                left = mid + 1
            else:
                right = mid
                
        return left