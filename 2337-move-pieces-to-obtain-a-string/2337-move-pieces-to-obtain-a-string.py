class Solution:
    def canChange(self, start: str, target: str) -> bool:
        left, right = {}, {}
        pieces = {}
        l = r = 0
        sl, el, sr, er = start.count("L"), target.count("L"), start.count("R"), target.count("R")
        for i in range(len(start)): #construct dictionary to keep relative position of start in target
            if start[i] == 'L':
                while l < len(target):
                    if target[l] == 'L':
                        if l > i:   return False
                        left[i] = l
                        pieces[i] = l
                        l += 1
                        break
                    l += 1
            if sl != el: return False
                    
            elif start[i] == 'R':
                while r < len(target):
                    if target[r] == 'R':
                        if r < i:   return False
                        right[i] = r
                        pieces[i] = r
                        r += 1
                        break
                    r += 1
            if sr != er: return False
                    
        
        leftStart = list(left.keys())   
        rightStart = list(right.keys())
        leftEnd = list(left.values())
        rightEnd = list(right.values())
        if len(leftStart) != len(leftEnd) or len(rightStart) != len(rightEnd):
            return False
        
        combStart = leftStart + rightStart
        combEnd = leftEnd + rightEnd
        combStart.sort();   combEnd.sort() #sort to see how they line up after change
        
        for i in range(len(combStart)):
            if pieces[combStart[i]] != combEnd[i]: #meaning there has been a cross over bn left and right if the sorting messes the order
                return False
            
        return True
        
        # print(leftStart, rightStart, leftEnd, rightEnd)
        # print(left, right, pieces)