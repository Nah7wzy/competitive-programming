class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        maxFreq = 1
        left, right = 0, 0
        prefixSum = 0 # to know how much left we need to increase for all previous values equal nums[right]
        while right < n:
            prefixSum += nums[right]
            
            while (nums[right] * (right - left + 1)) > prefixSum + k: #shrink window until left to right values can all become nums[right]
                prefixSum -= nums[left] 
                left += 1
                
            maxFreq = max(maxFreq, (right - left + 1))
            right += 1
                
        return maxFreq
        