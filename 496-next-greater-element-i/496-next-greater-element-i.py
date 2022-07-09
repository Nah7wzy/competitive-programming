class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono = []
        match = {}
        for i in nums2: #do a monotonic stack on nums2 and register next greater element in dictionary
            while mono and i > mono[-1]:
                match[mono.pop()] = i                
            mono.append(i)
            
        while mono: #remaining elements has no greater element
            match[mono.pop()] = -1
        
        res = []
        for i in nums1:
            res.append(match[i])
            
        return res