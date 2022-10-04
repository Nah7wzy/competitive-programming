class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pfx = nums
        sfx = nums[::-1]
        
        for i in range(1, len(nums)):
            pfx[i] = pfx[i] * (pfx[i-1] or 1) #if finds 0 then restart the prefix sum by giving it itself(mult by 1)
            sfx[i] = sfx[i] * (sfx[i-1] or 1)
         
        return max(max(pfx), max(sfx))