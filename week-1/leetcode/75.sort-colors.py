class Solution:
    def sortColors(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]   

x=Solution()
x.sortColors([2,0,2,1,1,0])