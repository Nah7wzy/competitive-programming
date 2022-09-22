class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def splits(roof):
            temp = nums[0]
            partitions = 1
            for i in range(1, len(nums)):
                if temp + nums[i] > roof:
                    partitions += 1
                    temp = 0
                temp += nums[i]
            return partitions
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if splits(mid) > m:
                left = mid + 1
            else:
                right = mid
                
        return left