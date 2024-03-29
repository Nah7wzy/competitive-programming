class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix) - 1, 0 #start from bottom left and move up or right conditionally
        
        while r >= 0 and c < len(matrix[0]):
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
            
        return False