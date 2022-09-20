class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        #bring positive integers to the beginning (to better handle marked indices later)
        a, b = 0, 0
        while b < n:
            if nums[b] <= 0:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
            b += 1
            
        for i in range(a, n): #track using nums values as index
            target = nums[i] if nums[i] >= 0 else -nums[i]  #if negative its marked so take the positive of the number
            target = target + a - 1
            if target < n:
                if nums[target] >= 0:
                    nums[target] *= -1
        
        res = 1
        for i in range(a, n):  #find the first unmarked index
            if nums[i] < 0:
                res += 1
            else:
                break
        
        return res
        