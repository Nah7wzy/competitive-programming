class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        nums.sort()
        x=len(nums)-k
        return str(nums[x])
#4min
x=Solution()
x.kthLargestNumber(["3","6","7","10"], 4)