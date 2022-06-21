class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        monoStack = []
        for i in asteroids:
            if i < 0:
                while monoStack and monoStack[-1] >=0 and monoStack[-1] < abs(i):
                    monoStack.pop()
                if monoStack and abs(i) == monoStack[-1]:
                    monoStack.pop()
                elif not monoStack or monoStack[-1] < 0:
                    monoStack.append(i)
            else:
                monoStack.append(i)
                        
        return monoStack