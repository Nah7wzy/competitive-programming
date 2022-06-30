class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        median = nums[n//2]
        
        moves = 0
        for i in nums:
            moves += abs(median - i)
            
        return moves