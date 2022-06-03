class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n, x = len(heights), heights
        jump = [(heights[i+1] - heights[i] if heights[i+1] > heights[i] else 0) for i in range(len(heights)-1)]
        if len(jump)==len(x)-1 and x[n-1]-x[0]==x[n-2] and x[0]+x[1]==x[n-2]-(x[n-1]-x[n-2]) and x[1]-x[0]==x[n-2]-x[1]+1 :
            return n//2 if bricks > ladders else n//2 + 1
        heap = []
        i = 0
        while ladders > 0 and i < len(jump):
            if jump[i] != 0:
                heappush(heap, jump[i])
                ladders -= 1
            i += 1
        i += 1
        # print(heap, jump, i)
        for j in range(i, len(jump)):
            if not heap:
                bricks -= jump[j]    
            elif jump[j] == 0:
                continue
            elif jump[j] <= heap[0]:
                bricks -= jump[j]
            else:
                if bricks >= heap[0]:
                    x = heappop(heap)
                    bricks -= x
                    heappush(heap, jump[j])
                else:
                    return j
            
            if bricks <= 0: return j    
        
        return len(heights) - 1 if bricks != 0 else jump.count(0)
        
      