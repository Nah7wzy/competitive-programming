class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if len(nums)==1 or k==0:
            pass
        else:
            lst=[]
            p1, p2 = 0, len(nums)-k
            while len(lst)<len(nums):
                lst.append(nums[(p1+(p2))%len(nums)])
                p1+=1

            for i in range(len(nums)):
                nums[i]=lst[i]

            
        
        