class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = set()
        
        left, right, res, total = 0, 0, 0, 0
        
        while right<len(nums):
            if nums[right] not in window:
                window.add(nums[right])
                total += nums[right]
                res = max(res, total)
            else:
                while nums[left] != nums[right]:
                    total -= nums[left]
                    window.remove(nums[left])
                    left+=1
                total -= nums[left]   
                window.remove(nums[left])
                left+=1
                continue
            right+=1
        
        return res