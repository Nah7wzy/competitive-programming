class Solution:
            
    lt20 = ["", "One", "Two", "Three", "Four", "Five", "Six","Seven", "Eight", "Nine", "Ten","Eleven", "Twelve",                                    "Thirteen","Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen","Nineteen"]

    tens = ["","Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty","Seventy", "Eighty", "Ninety"]
    
    thousands = ["", "Thousand", "Million", "Billion"]
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ans = ''
        i = 0
        while num > 0:
            if num % 1000 !=0:
                ans = self.helper(num%1000) +  Solution.thousands[i] + ' ' + ans
                
            num = num // 1000
            i+=1
            
        return ans.strip()
        
    def helper(self, num):
        if num < 20:
            return Solution.lt20[num] + ' ' if num != 0 else ''
        elif num < 100:
            return Solution.tens[num//10] + ' ' + self.helper(num%10)
        else:
            return Solution.lt20[num//100] + ' Hundred ' + self.helper(num%100)
        
                