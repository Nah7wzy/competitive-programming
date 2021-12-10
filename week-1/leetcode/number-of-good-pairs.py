class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        
        for i in range (len(nums)):
            k=i+1
            for j in range (k, len(nums)):
                if nums[i]==nums[j]:
                    count+=1
                    
        return count