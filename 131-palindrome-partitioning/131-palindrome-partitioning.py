class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def backtrack(i, partition):
            if i >= n:
                res.append(partition.copy())
                return
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
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