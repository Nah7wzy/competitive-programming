class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x = min(nums) #sum the difference of minimum no to the rest of the numbers
        moves = 0
        for i in nums:
            moves += (i-x)
            
        return moves
        
        
        
        
        
        
        
        
        
