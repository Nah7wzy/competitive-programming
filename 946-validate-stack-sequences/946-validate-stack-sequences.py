class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push, pop = 0, 0 #pointers
        reverse = False #to know when pushed stack reaches end and stop push increment
        n = len(pushed)
        
        if n==1:
            if pushed[0]==popped[0]:
                return True
            else:
                return False
                
        while pop < n:
            if push >= len(pushed):
                break
            if not reverse and pushed[push] == popped[pop]:
                pop += 1
                pushed.remove(pushed[push])
                
                push -= 1
                
                if push != -1 and pushed[push] == pushed[-1]:
                    reverse = True

                    push = -1
                if not reverse and push != -1:
                    push -= 1
                    
                
            elif reverse and pushed[-1] == popped[pop]:
                pushed.remove(pushed[-1])

                pop += 1
                
            elif reverse:
                pop += 1
                
            if not reverse:
                push += 1
                
        if pushed == []:
            return True
        else:
            return False
            
        
            