class KthLargest: #just keep a window of k large elements then when adding value 
                    #compare with the lowest of the window and return the lowest val

    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.nums = nums
        self.k = k
        
        for i in range(len(nums) - k):
            ans = heappop(self.nums)
        
    def add(self, val: int) -> int:
    
        if len(self.nums) < self.k or val > self.nums[0]:
            heappush(self.nums, val)
        
        if len(self.nums) > self.k:
            heappop(self.nums)
            
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)