class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = [x for x in nums] 
        stack.sort() #and find where it started to sort
        
        #count starting from first changed index to last changed index
        start, end = len(nums), 0
        for i in range(len(nums)):
            if stack[i] != nums[i]:
                start = min(start, i)
                end = max(end, i+1)
        
        return end - start if start < end else 0