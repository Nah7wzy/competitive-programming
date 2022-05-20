class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #use a hash to register prefix sum values and their count
        #use this count to know how many subs in a larger sub array have a sum of the difference bn the sum and k
        #this dif means there exists a sub that result in same k value
        
        h = {0:1}
        res, presum = 0, 0
        
        for i in nums:
            presum += i
            if presum-k not in h:
                if presum in h:
                    h[presum] += 1
                else:
                    h[presum] = 1
            else:
                res += h[presum-k]
                if presum in h:
                    h[presum] += 1
                else:
                    h[presum] = 1
        print(h)      
        return res
                
                    