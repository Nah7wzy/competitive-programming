class Solution: #20
    def findDuplicate(self, nums: List[int]) -> int:
        #binary search 1 to n looking in nums for each how many values are lower, if the count is greater than the expected 1 to x count, that means a value is duplicate below x
        n = len(nums)
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            total = 0
            for i in nums:
                total += 1 if i <= mid else 0
            
            if total > mid:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return res
        