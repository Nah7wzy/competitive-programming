class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def roofn(x): #find the roof of power of 2 number for current k
            return math.log2(x)
        
        #since every half is a reverse of previous, count how many times we reversed 0 backwards (if even 0 itself else 1)
        steps = 0
        while k > 1:
            i = roofn(k)
            k -= math.pow(2, math.ceil(i-1))
            steps += 1
        
        return 0 if steps % 2 == 0 else 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = "0"
#         for i in range(5):
#             temp = ""
#             for x in res:
#                 if x == "0":
#                     temp += "01"
#                 elif x == "1":
#                     temp += "10"
                    
#             res = temp
            
#         print(res)
                    