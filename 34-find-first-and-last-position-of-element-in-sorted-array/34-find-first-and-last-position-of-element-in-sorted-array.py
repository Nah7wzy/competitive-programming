class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        start = -1
        end = -1
        
        #compute for start
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                start = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        #compute for end
        if start == -1: return [-1, -1]
        left, right = start, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                end = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return [start, end]
        
        