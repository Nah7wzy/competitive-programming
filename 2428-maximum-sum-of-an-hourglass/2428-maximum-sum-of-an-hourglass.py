class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid) - 2):
            l, m, r = 0, 1, 2
            while r < len(grid[0]):
                total = grid[row+1][m]
                for i in range(l, r+1):
                    total += grid[row][i]
                    total += grid[row+2][i]
                res = max(res, total)
                l, m, r = l+1, m+1, r+1
        
        return res