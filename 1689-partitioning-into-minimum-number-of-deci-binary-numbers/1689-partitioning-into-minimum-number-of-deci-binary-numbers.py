class Solution:
    def minPartitions(self, n: str) -> int:
        res = [int(i) for i in n]
        return max(res)