class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        #take the best solution of k previous values..and add it to current..as the previous were done the same landing
        #on that value shows the result of jumping there
        heap = [(-nums[0],0)]
        n = len(nums) 
        
        for i in range(1, n):
            while heap[0][1] < i-k: #remove the max element that is out of range for the current element
                heappop(heap)
            top = heap[0][0]
            heappush(heap, (top - nums[i], i))
           
            if i == n-1:
                return - (top - nums[i])
        
        return nums[0]