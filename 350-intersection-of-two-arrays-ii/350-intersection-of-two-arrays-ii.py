class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not len(nums1) <= len(nums2):
            nums1, nums2 = nums2, nums1
        nums2.sort()
        ans = []
        for i in nums1:
            left, right = 0, len(nums2) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums2[mid] == i:
                    ans.append(i)
                    nums2.remove(nums2[mid])
                    break
                elif nums2[mid] > i:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return ans