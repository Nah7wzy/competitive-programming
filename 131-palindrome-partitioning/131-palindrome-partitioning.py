class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        dp = {}
        def backtrack(i, partition):
            if i >= n:
                res.append(partition.copy())
                return
            for j in range(i, n):
                if (i, j) in dp:
                    valid = dp[(i,j)]
                else:
                    valid = self.isPalindrome(s, i, j)
                    dp[(i,j)] = valid
                if valid:
                    partition.append(s[i:j+1])
                    backtrack(j + 1, partition)
                    partition.pop()
                    
        backtrack(0, [])
        return res
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True