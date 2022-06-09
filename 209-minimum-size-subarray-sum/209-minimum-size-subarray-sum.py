class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currMin, currSum = len(nums) + 1, 0
        a, b = 0, 0
        
        while a <= b and b < len(nums):
            currSum += nums[b]
            if currSum >= target:
                currMin = min(currMin, b - a + 1)
                currSum -= nums[a]
                a += 1
                currSum -= nums[b]
            else: 
                b += 1
                
        return currMin if currMin <= len(nums) else 0