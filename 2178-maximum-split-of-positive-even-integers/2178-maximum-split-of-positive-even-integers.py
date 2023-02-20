class Solution:
    def maximumEvenSplit(self, n: int) -> List[int]:
        res = []
        if n % 2 == 0:
            start = 2
            total = 0
            while total < n:
                if n - total - start > start or n - total - start == 0:
                    res.append(start)
                    total += start
                    start += 2
                else:
                    start += 2
            return res if res else [n]
        return res