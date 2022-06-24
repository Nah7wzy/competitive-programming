class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        neighbors = {}
        
        for i in range(1, len(nums) - 1):
            j = i
            if nums[i] == nums[i-1]: #avoid double count for flat
                continue
                
            while j < len(nums) - 1 and nums[j+1] == nums[i]: #avoid flat surfaces
                j += 1
            if j + 1 < len(nums):
                neighbors[i] = (i-1, j+1)
            
        count = 0
        for x in neighbors:
            left, right = neighbors[x]
            if nums[left] < nums[x] > nums[right] or nums[left] > nums[x] < nums[right]:
                count += 1
                
        return count