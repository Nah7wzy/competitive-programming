class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        @cache
        def dp(i, j, k):
            if i > j: #no boxes
                return 0
            
            #find where the consecutive boxes end
            l = i + 1
            while l <= j and boxes[l] == boxes[i]:
                l += 1
                k += 1                
            
            points = (k+1) * (k+1) + dp(l, j, 0) #removing the current consecutive boxes
            for next_appearance in range(l, j+1):
                if boxes[next_appearance] == boxes[i]:
                    #calculate if just removing the previous boxes and restarting is better or continuing from previous
                    #second option = remove in bn + carry k from prev and do operation
                    remove_together = dp(l, next_appearance - 1, 0) + dp(next_appearance, j, k+1)
                    points = max(points, remove_together)
                    
            return points
        
        return dp(0, n-1, 0)
            
                
                
        