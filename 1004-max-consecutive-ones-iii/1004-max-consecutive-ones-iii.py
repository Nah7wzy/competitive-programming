class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left =  maxl = 0
        
        for i in range(len(nums)):
            if nums[i]==0:
                if k > 0:
                    k-=1
                else:
                    maxl=max(maxl, i-left)
                    while nums[left] == 1 and left < i:
                        left+=1
                    left+=1
        print(i)
        maxl=max(maxl, i-left+1)
        return maxl
                
                
                