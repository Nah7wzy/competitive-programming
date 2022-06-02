class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapify(stones)
        
        while len(stones) > 1:
            x = heappop(stones)
            y = heappop(stones)
            
            if x != y:
                heappush(stones, (x-y))
            
        return -(heappop(stones)) if len(stones) == 1 else 0
                