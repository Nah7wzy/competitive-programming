class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people) #start with shortest and place by reserving spots for further tallest
        res = [-1] * n
        
        people.sort()
        for i in people:
            countOfSpace = j = 0
            if i[1] == 0:
                while res[countOfSpace] != -1:
                    countOfSpace += 1
                res[countOfSpace] = i
            else:
                while j < n:
                    if res[j] == -1 or res[j][0] == i[0]:
                        countOfSpace += 1
                    if countOfSpace > i[1]:
                        break
                    j += 1
            
                res[j] = i
            
        return res