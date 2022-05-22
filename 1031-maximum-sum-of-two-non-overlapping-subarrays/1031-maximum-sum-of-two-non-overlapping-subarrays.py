class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums [i]
        
        ptr1, ptr2 = 0, firstLen
        maxSum = 0
        
        while ptr2<=len(nums):
            currSum = (nums[ptr2-1] - nums[ptr1-1]) if ptr1 != 0 else (nums[ptr2-1])
            currWin = (ptr1, ptr2)
            ptra, ptrb = 0, secondLen
            
            while ptrb<=len(nums):
                if ptra <= ptr2-1 and ptrb-1 >= ptr1: #check window overlap
                    pass
                else:
                    checkSum = (nums[ptrb-1] - nums[ptra-1]) if ptra != 0 else (nums[ptrb-1])
                    maxSum = max(maxSum, (currSum + checkSum))
                    
                ptra+=1
                ptrb+=1
                
            ptr1+=1
            ptr2+=1
            
        return maxSum