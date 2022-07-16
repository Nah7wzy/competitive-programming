class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ''.join(str(e) for e in digits)
        res = int(x) + 1
        return [i for i in str(res)]