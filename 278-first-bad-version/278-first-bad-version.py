# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution: #10
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
                
        return ans