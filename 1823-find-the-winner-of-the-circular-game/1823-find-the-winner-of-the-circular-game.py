class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = list(range(1,n+1))
        
        def recur(i):
            if len(circle) == 1:
                return circle[0]
            new_index = (i + k - 1) % len(circle)
            circle.remove(circle[new_index])
            return recur(new_index)
            
        return recur(0)
            
        