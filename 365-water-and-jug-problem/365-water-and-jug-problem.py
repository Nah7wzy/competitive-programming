class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        direction = [jug1Capacity,-jug1Capacity, jug2Capacity, -jug2Capacity ]
        q = deque([0])
        visited = set([0])
        
        while q:
            x = q.popleft()
            for value in direction:
                cur = value + x
                if 0 < cur <= jug1Capacity + jug2Capacity and cur not in visited:
                    if cur == targetCapacity:
                        return True
                    q.append(cur)
                    visited.add(cur)        
        return False
            
            
            
            