class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = sum(matchsticks) // 4 #length of each side expected
        sides = [0] * 4
        
        if sum(matchsticks) / 4 != n: #means needs breaking or one piece is too long to be a side
            return False
        
        matchsticks.sort(reverse = True)
        def place(x):
            if x == len(matchsticks):
                return True
            
            for i in range(4):
                if sides[i] + matchsticks[x] <= n:
                    sides[i] += matchsticks[x]
                    if place(x + 1):
                        return True
                    sides[i] -= matchsticks[x] #backtrack after trying out a placement one one of sides
                    
            return False
        
        return place(0)
        