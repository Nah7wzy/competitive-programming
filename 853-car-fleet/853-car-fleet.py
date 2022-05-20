class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #use a sorted list of position in reverse so that we can iteratively check previous cars
        stack = []
        x = sorted(zip(position, speed), reverse=True)
        
        #if time takes longer starting from back it means it wont catch up so added to stack as a fleet
        #if otherwise finish time taking less from back means it catches up so no need to add
        
        for i, ps in enumerate(x):
            time = (target-ps[0])/ps[1]
            
            if not stack or time > stack[-1]:
                stack.append(time)
                
        return len(stack)
        