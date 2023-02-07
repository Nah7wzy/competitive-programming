class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'G':
                x, y = x + dx, y + dy
            elif i == 'L':
                dx, dy = -dy, dx
            elif i == 'R':
                dx, dy = dy, -dx
        #if the robot keeps repeating the instructions, it will either remain at the starting point (0, 0), or it will have turned 180 degrees
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)