class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1, c1, r1, c2 = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        
        while l1 <= r1 and c1 <= c2:
            mid1 = l1 + (r1 - l1) // 2
            mid2 = c1 + (c2 - c1) // 2
            
            if matrix[mid1][mid2] == target:
                return True
            elif matrix[mid1][mid2] > target:
                if matrix[mid1][0] > target:
                    r1 = mid1 - 1
                else:
                    c2 = mid2 - 1
                
            else:
                if matrix[mid1][len(matrix[0]) - 1] < target:
                    l1 = mid1 + 1
                else:
                    c1 = mid2 + 1
                
        return False