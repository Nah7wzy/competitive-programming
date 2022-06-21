class Solution:
    def candy(self, ratings: List[int]) -> int:
        distribution = [1] #go left to right and register based on left neighbor and return from right and update if necessary
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                distribution.append(distribution[i-1] + 1)
            else:
                distribution.append(1)
     
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1] and distribution[i] <= distribution[i + 1]:
                distribution[i] = distribution[i+1] + 1
        
        return sum(distribution)