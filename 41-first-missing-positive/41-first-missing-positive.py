class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        first = 1
        for num in nums:
            if num > 0:
                if num > first:
                    return first
                elif num == first:
                    first += 1
                    
        return first