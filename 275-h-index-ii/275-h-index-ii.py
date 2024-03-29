class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # find the min index such that citations[i] >= len(citations) - i
        n = len(citations)
        l, r = 0, n - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
                
        return n - l
                