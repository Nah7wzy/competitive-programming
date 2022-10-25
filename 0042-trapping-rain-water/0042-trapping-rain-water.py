class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        monostack = [height[0]]
        total = 0
        for i in range(1, n):
            if height[i] <= monostack[-1]:
                monostack.append(height[i])
            else:
                tempstack = []
                while monostack and height[i] > monostack[-1]:
                    last = monostack.pop()
                    if monostack:
                        fill = min(monostack[0], height[i]) - last
                        tempstack.append(fill + last)
                        total += fill                        
                        
                while monostack and tempstack: #pop fill then append the new height so as to add on it later if taller wall comes
                    monostack.append(tempstack.pop())
                
                monostack.append(height[i])
        return total
                    