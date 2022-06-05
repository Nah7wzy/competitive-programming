class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = 0, 0
        ans = 0
        
        while b < len(nums2) and a < len(nums1):
            if nums1[a] <= nums2[b]:
                ans = max(ans, b - a)
                b += 1
            else:
                a += 1
                if a > b:
                    b = a
                    
        return ans