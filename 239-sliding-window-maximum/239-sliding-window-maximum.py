class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() #monotonic queue that dont need to be size of k
        ans = []
        
        for i, num in enumerate(nums):
            while q and num > q[-1][0]:
                q.pop()
            q.append((num, i))
            
            while q and i - q[0][1] > k - 1: #if out of window
                q.popleft()
            
            if i >= k - 1: #minimum window reached
                ans.append(q[0][0])
                
        return ans
                