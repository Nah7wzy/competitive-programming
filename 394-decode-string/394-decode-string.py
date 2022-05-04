class Solution: #80min
    def decodeString(self, s: str) -> str:
        temp = ''
        temp_no= 0
        stack = []
        for i in s:
            if i == '[':
                stack.append((temp, temp_no)) #keep the string and multiplier together
                temp = '' 
                temp_no = 0 #reset after appending current string
                
            elif i == ']':
                string, counter = stack.pop()
                temp= string + temp*counter #append on the previous string by multiplying the new one with saved counter
                
            elif i.isdigit():
                x=int(i)
                temp_no*=10 #if its more than ones it keep track of the digit place
                temp_no+=x #add it to ones place
                    
            else:
                temp+=i
            
        return temp