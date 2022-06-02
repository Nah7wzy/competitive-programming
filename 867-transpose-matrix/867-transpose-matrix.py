class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        transpose = [[] for i in range(c)]
        i, j = 0, 0
        
        while True:
            transpose[j].append(matrix[i][j])
            if i == r - 1 and j != c - 1:
                i = 0
                j += 1
            elif i == r - 1 and j == c - 1:
                break
            else:
                i += 1
                
        return transpose
            