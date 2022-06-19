class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        monoq = deque()
        minLen = float('inf')
        for x in nums:
            prefixSum.append(x + prefixSum[-1])
            
        for idx, cur in enumerate(prefixSum):
            while monoq and prefixSum[monoq[-1]] >= cur:  #maintain monotonic queue to calculate for sum inc values (positive)
                monoq.pop() 

            while monoq and cur - prefixSum[monoq[0] ]>= k:  #traverse from left until curr - that left is still >=k
                minLen = min(minLen, idx - monoq.popleft()) 
                
            monoq.append(idx) #we add index bc there will be negative values in bn which will affect the length.
            
        return -1 if minLen == float('inf') else minLen