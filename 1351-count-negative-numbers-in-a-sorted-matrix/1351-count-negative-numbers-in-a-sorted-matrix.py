class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for x in grid:
            m, n = 0, len(grid[0])
            while m < n:
                mid = m + (n - m) // 2
                if x[mid] < 0:
                    n = mid
                else:
                    m = mid + 1
            cnt += len(x) - m
            
        return cnt