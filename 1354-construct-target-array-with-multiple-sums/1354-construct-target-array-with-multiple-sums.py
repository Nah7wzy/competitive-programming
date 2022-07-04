class Solution:
    def isPossible(self, target: List[int]) -> bool:
        target.sort(reverse=True)
        heap = [-i for i in target]
        
        while heap[0] != -1:
            
            curr = heappop(heap)
            curr_sum = sum(heap)

            if curr_sum == -1:
                return True
            if curr_sum <= curr or curr_sum == 0 or curr % curr_sum == 0:
                return False
            
            curr %= curr_sum
            heappush(heap, curr)
            
        return True
        
        