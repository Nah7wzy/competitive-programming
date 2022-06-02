class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [] #use heap to traverse through rows based on their left element value popping the smallest for each k
        
        for row in matrix:
            heappush(heap, (row[0], 0, row)) #start with 0 col and save arr for col traversal
        
        while k > 0 and heap:
            val, i, arr = heappop(heap)
            if i + 1 < n:
                heappush(heap, (arr[i+1], i+1, arr))
            k -= 1
            
        return val
        