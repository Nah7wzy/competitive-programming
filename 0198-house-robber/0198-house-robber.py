class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        for i in range(2, n):
            nums[i] = max(nums[i-1], nums[i] + nums[i-2], nums[i] + nums[i - 3] if i >= 3 else 0)
        return nums[-1]