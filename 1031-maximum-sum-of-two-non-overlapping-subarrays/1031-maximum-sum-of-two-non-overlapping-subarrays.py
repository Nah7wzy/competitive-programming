class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        ps = [0]
        for i in range(len(nums)):
            ps.append(ps[-1] + nums[i])
            
        a1, b1, a2, b2 = 1, firstLen, 1, secondLen
        res = 0
        while b1 < len(ps):
            while b2 < len(ps):
                if b2 < a1 or a2 > b1:  #no overlap
                    cur_sum = (ps[b1] - ps[a1 - 1]) + (ps[b2] - ps[a2 - 1])
                    res = max(res, cur_sum)
                a2, b2 = a2 + 1, b2 + 1
            a2, b2 = 1, secondLen
            a1, b1 = a1 + 1, b1 + 1
            
        return res