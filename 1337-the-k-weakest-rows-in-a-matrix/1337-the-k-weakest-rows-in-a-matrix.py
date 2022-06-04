class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        minHeap = [(x.count(1), i) for i, x in enumerate(mat)]
        heapify(minHeap)
        ans = []
        while k > 0:
            ans.append(heappop(minHeap)[1])
            k -= 1
            
        return ans
        