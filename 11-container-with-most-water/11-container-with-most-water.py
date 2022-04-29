class Solution:
    def calc(self, i, j, x, y):
        return abs(j-i)*min(x, y)
    
    def maxArea(self, height: List[int]) -> int:
        
        n=len(height)
        a,b=0,n-1
        max = 0

        while a<b:
            
            if self.calc(a, b, height[a], height[b]) > max:
                max = self.calc(a, b, height[a], height[b])
            if height[a]<height[b]:
                a+=1
            else:
                b-=1
                
        return max
            