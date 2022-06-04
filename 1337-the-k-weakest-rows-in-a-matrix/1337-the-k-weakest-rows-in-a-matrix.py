class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        minHeap = [(self.findOnes(x), i) for i, x in enumerate(mat)]
        heapify(minHeap)
        ans = []
        
        while k > 0:
            ans.append(heappop(minHeap)[1])
            k -= 1
        
        return ans
    
    #use binary search to find count of ones and heap for strength
    def findOnes(self, arr):
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] == 1:
                left = mid + 1
            else:
                right = mid
                
        return right
        