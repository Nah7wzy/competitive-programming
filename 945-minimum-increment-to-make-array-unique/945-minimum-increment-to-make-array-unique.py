class Solution:        
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count=0
        nums.sort() #bring same values together
        steps=nums[0] #when same value keeps adding 1 to next value to know how much to add for each value to escape the group of same values (the more number of unique values the more step needed for each)
        
        for i in nums:
            if i<steps: #less means it was same value since it didnt pass 1 increment
                count+=steps-i # extracts the steps from base value
                steps+=1
            else:
                steps = i+1 #if not same then we update +1 on the current value to check with                              the upcoming
        
        return count