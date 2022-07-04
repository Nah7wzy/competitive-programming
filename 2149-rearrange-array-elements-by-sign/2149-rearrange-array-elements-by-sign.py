class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = [], []
        for x in nums:
            positive.append(x) if x > 0 else negative.append(x)
        
        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(positive[i // 2])
            else:
                res.append(negative[i // 2])
                
        return res