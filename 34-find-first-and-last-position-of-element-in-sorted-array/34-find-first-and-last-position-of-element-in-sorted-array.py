class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        res= [-1, -1]
        
        def bs(l, r, pos):
            if l > r:
                return 
            
            mid = l + (r - l) // 2
            if nums[mid] > target:
                bs(l, mid - 1, pos)
            elif nums[mid] < target:
                bs(mid + 1, r, pos)
            else:
                if pos == 0:
                    res[0] = mid
                    bs(l, mid -1 , pos)
                elif pos == 1:
                    res[1] = mid
                    bs(mid + 1, r, pos)
                    
        bs(l, r, 0)
        bs(l, r, 1)
        return res
        
        
