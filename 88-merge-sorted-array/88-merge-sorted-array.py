class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m + n - 1
        a, b = m-1, n-1
        while a >= 0 and b >= 0:
            if nums2[b] >= nums1[a]:
                nums1[end] = nums2[b]
                b -= 1
            else:
                nums1[end] = nums1[a]
                a -= 1
            
            end -= 1
            
        while b >= 0:
            nums1[end] = nums2[b]
            b -= 1
            end -= 1
                