class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix, postfix = [nums[0]], [nums[-1]]
        for i in range(1, n):
            prefix.append(prefix[-1] + nums[i])
            postfix.append(postfix[-1] + nums[n - i -1])
        
        def calc(x):
            avg1 = prefix[i] // (i + 1)
            avg2 = postfix[n - i - 2] // (n - i - 1) if n != i + 1 else 0
            return abs(avg1 - avg2)
            
        mad = float('inf')
        res = 0
        for i in range(n):
            x = calc(i)
            if x < mad:
                mad = x
                res = i
                
        return res