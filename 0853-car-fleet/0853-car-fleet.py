class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = {}
        for i in range(len(position)):
            #register arriving time for each position
            time_taken = (target - position[i]) / speed[i]
            time[position[i]] = time_taken
            
        position.sort(reverse = True) #start from closest and find cars that are farther but take less or equal time
        stack = []
        for pos in position:
            if stack and time[pos] <= time[stack[-1]]:
                continue
            stack.append(pos)
            
        return len(stack)