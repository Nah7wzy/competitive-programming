class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = []
        while digits and digits[-1] >= 9:
            digits.pop()
            temp.append(0)
        if digits:
            digits.append(digits.pop() + 1)
        else:
            digits.append(1)
        
        while temp:
            digits.append(temp.pop())
            
        return digits
            