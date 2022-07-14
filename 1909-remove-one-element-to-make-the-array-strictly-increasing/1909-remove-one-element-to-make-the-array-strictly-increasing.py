class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def isIncreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i + 1] <= arr[i]:
                    return False
            return True
        
        for x in range(len(nums)):
            if isIncreasing(nums[:x] + nums[x + 1 ::]):
                return True
            
        return False
            