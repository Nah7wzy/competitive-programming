class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = ''
        for i in range(1, len(nums)):
            if direction == '':
                if nums[i] > nums[i-1]: direction = 'up'
                if nums[i] < nums[i-1]: direction = 'down'
                    
            if (direction == 'up' and nums[i] < nums[i-1]) or (direction == 'down' and nums[i] > nums[i-1]):
                return False
            
        return True
                