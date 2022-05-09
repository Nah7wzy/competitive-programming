class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = list(range(1,n+1))
        i=0
        while len(circle)!=1:
            i+=(k-1)
            if i>=len(circle):
                while i>=len(circle):   
                    i=i-len(circle)
            # print(circle[i],i)
            circle.remove(circle[i])
            
        return circle[0]
            
        