class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        maxHeight = horizontalCuts[0]
        maxWidth = verticalCuts[0]
        for i in range(len(horizontalCuts)-1):
            maxHeight = max(maxHeight, horizontalCuts[i+1] - horizontalCuts[i])
            
        for i in range(len(verticalCuts)-1):
            maxWidth = max(maxWidth, verticalCuts[i+1] - verticalCuts[i])
            
        return (maxHeight * maxWidth) % (pow(10, 9) + 7)