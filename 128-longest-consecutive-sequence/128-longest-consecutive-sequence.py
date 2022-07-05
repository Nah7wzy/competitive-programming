class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = {}
        for i in nums:
            seq[i] = i + 1
        
        dp = {}
        ans = 0
        for j in seq:
            count = 0
            x = j
            while seq[x] in seq:
                if x in dp:
                    count += dp[x]
                    break
                else:
                    count += 1
                    x += 1
            
            dp[j] = count
            ans = max(ans, count + 1)
        # print(dp)
            
        return ans
                