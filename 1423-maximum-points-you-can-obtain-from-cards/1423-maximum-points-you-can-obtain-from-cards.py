class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        #establish two prefix sum from left and right until k, j + i = k 
        left = [0]
        right = [0]
        
        for i in range(k):
            left.append(cardPoints[i] + left[-1])
            right.append(cardPoints[n-i-1] + right[-1])
         
        #(start assuming we choose only form one side) then traverse out from one while going in from the other
        score = right[-1]
        j = 0
        
        for i in range(k+1):
            score = max(score, right[k-i] + left[j])
            j += 1
            
        return score