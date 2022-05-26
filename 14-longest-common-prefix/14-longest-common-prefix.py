class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        i = 0
        curr = ""
        n = len(min(strs))
        
        while i < n:
            for j in range(len(strs)):
                if j == 0:
                    curr = strs[j][i]
                    # print(curr)
                if strs[j][i] != curr:
                    return ans
            ans += curr
            i+=1
            
        return ans
            