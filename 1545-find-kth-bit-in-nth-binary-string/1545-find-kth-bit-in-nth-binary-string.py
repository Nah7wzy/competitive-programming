class Solution:
    def invert(self, x):
        res = ""
        for i in x:
            if i == "0":
                res+="1"
            else:
                res+="0"
        return res

    def reverse(self, y):
        return y[::-1]

    def binaryString(self, n):
        if n == 1:
            return "0"
        s=self.binaryString(n-1)

        return s+"1"+self.reverse(self.invert(s))

    def findKthBit(self, n: int, k: int) -> str:
        
        return self.binaryString(n)[k-1]
