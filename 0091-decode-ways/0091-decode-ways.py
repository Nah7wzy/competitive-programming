class Solution:
    def numDecodings(self, s: str) -> int:
        #if it can be two digits pull from next to last digit and add it to prev digit bc the pulled ones are the ones that can go with the two digits (bottom-up starting from last digit) (simply visualise adding only single digit and also treating it as two digits to the next one - then see where u start next for each scenario (left to right))
        n = len(s)
        dp = [1] * (n + 1)
        
        for i in range(n - 2, -1, -1):
            single = dp[i + 1]
            if s[i+1] == '0':
                if int(s[i]) > 2 or s[i] == '0':
                    return 0
                else:
                    dp[i] = single
                    
            elif int(s[i]) > 0 and int(s[i] + s[i+1]) <= 26:
                if i < n - 2 and s[i+2] == '0':
                    dp[i] = single
                else:
                    dp[i] = (single + dp[i+2])
                
            else:
                dp[i] = single
       
        return dp[0] if s[0] != '0' else 0
    
    '''"12"
"226"
"06"
"206"
"306"
"2101"
"21001"'''