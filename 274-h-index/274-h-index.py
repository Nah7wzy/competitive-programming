class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        for i, x in enumerate(citations):
            if x<=i:
                return i
                
        return len(citations)