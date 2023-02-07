class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        
        while len(nums) > k-1:
            x = heappop(nums)
        
        return x