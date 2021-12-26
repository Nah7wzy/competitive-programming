class Solution:
    def rearrangeArray(self, nums):
        for i in range (1,len(nums)-1):
            if (nums[i-1]<nums[i]<nums[i+1])or (nums[i-1]>nums[i]>nums[i+1]):
                nums[i+1],nums[i]=nums[i],nums[i+1]
        return nums

x=Solution()
print(x.rearrangeArray([1,2,3,4,5]))