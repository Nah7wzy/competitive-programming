class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        lst = [num % 2 for num in nums]
        presum = 0
        odd = 0
        
        d = {0:1}
        print(lst)
        for i in lst:
            presum += i
            if presum - k in d:
                odd += d[presum-k]
                
            if presum in d:
                d[presum] += 1
            else:
                d[presum] = 1
                
        return odd