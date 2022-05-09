class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_s=0
        col_en=len(matrix[0]) #to keep track of row and col movement
        row_en=len(matrix)
        col_s=0
        answer = []
        
        #there will be 4 movs of along the edges and we will keep squeezing the box in
        #and doing the same loop until start meets end halfway
        
        while row_s<row_en and col_s<col_en:
            
            #print first row
            
            for i in range(col_s, col_en):
                answer.append(matrix[row_s][i])              
            row_s+=1 #move row down
            
            #print last column
            for i in range(row_s, row_en):
                answer.append(matrix[i][col_en-1])
            col_en-=1 #move column end left
            
            if row_s<row_en:
                #print last row by going reverse
                for i in range(col_en-1, col_s-1, -1):
                    answer.append(matrix[row_en-1][i])
                row_en-=1 #move row up
                
            if col_s<col_en:
                #print first column by going reverse
                for i in range(row_en-1,row_s-1,-1):
                    answer.append(matrix[i][col_s])
                col_s+=1 #move column right
                
        return answer
                
            
            
        