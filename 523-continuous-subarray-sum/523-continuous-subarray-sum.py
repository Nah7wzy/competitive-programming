class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        rem = {0:0}
        for i, num in enumerate(nums):
            if num % k in rem and abs(rem[num % k] - i) > 0:
                return True
            if num % k not in rem:
                rem[num % k] = i + 1 #double standards for sum begining from 0 and in the middle
        return False