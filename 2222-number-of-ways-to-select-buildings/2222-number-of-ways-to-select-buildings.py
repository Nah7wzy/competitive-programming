class Solution:
    def numberOfWays(self, s: str) -> int:
        n0, n1, n01, n10, n010, n101 = [0], [0], [0], [0], [0], [0]
        
        for bit in s:
            if bit == '1':
                n1.append(n1[-1] + 1)
                n01.append(n01[-1] + n0[-1])
                n101.append(n101[-1] + n10[-1])
            else:
                n0.append(n0[-1] + 1)
                n10.append(n10[-1] + n1[-1])
                n010.append(n010[-1] + n01[-1])
                
        # print(n0,n1,n01,n10,n101,n010)        
        return n101[-1] + n010[-1]