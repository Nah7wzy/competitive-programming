class Solution:
    def targetIndices(self, nums, target):
        answer=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                answer.append(i) 
            
        return answer