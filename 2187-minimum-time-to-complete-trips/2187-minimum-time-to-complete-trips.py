class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        #worst case the fastest bus takes all the trips
        l, r = 1, min(time) * totalTrips
        
        while l < r:
            mid = (l + r) // 2
            
            total = 0
            for t in time:
                total += mid//t
           
            if total >= totalTrips:
                r = mid
            else:
                l = mid + 1
                
        return l
            