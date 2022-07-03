class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        direction = -1 #keep what should appear next and go until it wiggles then change direction
        count = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if direction == -1 and diff != 0:
                direction = diff < 0
                count += 1
                continue
                
            if (diff < 0) != direction and diff != 0:
                count += 1
                direction = diff < 0
      
        return count
            
            