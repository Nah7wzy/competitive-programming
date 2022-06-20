class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:  return nums[0]
        @cache
        def dp1(i):
            if i >= n - 1:
                return 0
            money = nums[i]
            return max(money + dp1(i + 2), dp1(i+1))
        @cache
        def dp2(i):
            if i >= n:
                return 0
            money = nums[i]
            return max(money + dp2(i + 2), dp2(i+1))
        
        return max(dp1(0), dp2(1))