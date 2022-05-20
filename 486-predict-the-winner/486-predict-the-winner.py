class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
         
        return True if self.helper(nums) >= 0 else False
    
    def helper (self, nums):
        
        if len(nums) < 2:
            return nums[0]
        else:
            return max(nums[0] - self.helper(nums[1::]), nums[-1] - self.helper(nums[:-1]))