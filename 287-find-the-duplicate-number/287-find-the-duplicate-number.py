class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        left, right = 0, n-1
        
        while left < right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] >= mid + 1:
                left = mid
            elif nums[mid] < mid + 1:
                right = mid
                
            if nums[left] == nums[right]:   return nums[left]