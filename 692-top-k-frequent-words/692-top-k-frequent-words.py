class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        heap = [(-x[1], x[0]) for x in d.items()]
        heapify(heap)
        ans = []
        
        while len(ans) < k:
            ans.append(heappop(heap)[1])
        
        return ans