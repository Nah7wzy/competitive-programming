class Solution:
    def trap(self, height: List[int]) -> int: 
        n = len(height) 
        #register how much water one height can hold above it by using taller environments to the left and right
        maxLeft, maxRight = [0] * n, [0] * n
        currMax = currMax2 = 0
        
        for i in range(n):
            maxLeft[i] = currMax
            if height[i] > currMax: currMax = height[i]
        for j in range(n-1, -1, -1):
            maxRight[j] = currMax2
            if height[j] > currMax2: currMax2 = height[j]
        
        res = 0
        for i in range(n):
            x = min(maxLeft[i], maxRight[i]) - height[i]
            if x > 0:
                res += x
           
        return res
                