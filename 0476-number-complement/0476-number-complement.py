class Solution:
    def findComplement(self, num: int) -> int:
        aymen = 1
        for i in range(num.bit_length()):
            num ^= aymen
            aymen = aymen << 1
        
        return num