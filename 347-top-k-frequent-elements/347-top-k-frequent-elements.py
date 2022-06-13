class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        heap = [(-x[1], x[0]) for x in d.items()]
        heapify(heap)
        ans = []
        
        while len(ans) < k:
            ans.append(heappop(heap)[1])
        
        return ans