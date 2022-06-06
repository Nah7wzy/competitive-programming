class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i+1] < nums[i]:
                return nums[i+1]
            
        return nums[0]