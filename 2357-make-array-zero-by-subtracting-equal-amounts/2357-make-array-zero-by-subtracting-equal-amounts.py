class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        res = 0
        while total > 0:
            x = -1
            for i, num in enumerate(nums):
                if x == -1 and num > 0:
                    x = num
                if x != -1:
                    nums[i] = nums[i] - x
                    total -= x
            res += 1
        return res
        