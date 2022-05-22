class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #use one loop to record previous then start from end to finish the remaining
        result = [1]*len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i] #increment for next number assignment
            
        for j in range(len(nums)-1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]
            
        return result