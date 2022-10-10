class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        a, b = max(a, b), min(a, b)
        res = 0
        for i in range(1, b + 1):
            res += 1 if (a%i == 0 and b%i == 0) else 0
        return res