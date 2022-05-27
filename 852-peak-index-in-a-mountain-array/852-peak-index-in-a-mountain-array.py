class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            if arr[i+1] >= arr[i]:
                ans = i + 1
            else:
                return ans
            
            