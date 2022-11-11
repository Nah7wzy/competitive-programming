class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        first_sig_bit = (x & (x-1)) ^ x # finds the first appearance of bit 1
        
        a = x
        for num in nums:
            if num & first_sig_bit:
                a ^= num
                
        return [a, a ^ x]