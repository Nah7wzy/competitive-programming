class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @cache
        def dp(i):
            if i >= n: #base case
                return 0
            point, bp = questions[i] 
            
            return max(point + dp(i + bp + 1), dp(i + 1)) #max of current plus skip or choose not to solve current
        
        return dp(0)