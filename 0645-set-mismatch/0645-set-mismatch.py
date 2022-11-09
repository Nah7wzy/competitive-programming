class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        prev = 0
        res = [-1, -1]
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                res[0] = num
            if num - prev > 1:
                res[1] = num - 1
            prev = num
        
        return res if res[1] != -1 else [res[0], len(nums)]