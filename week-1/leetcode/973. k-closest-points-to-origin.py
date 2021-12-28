class Solution:
    def calculate_d(self, arr):
        return (((arr[0])**2) + ((arr[1])**2))**0.5
    def kClosest(self, points, k):
        
        answer=points[:]
        mink=[] #to keep the respective distances
        for i in points:
            cur = self.calculate_d(i)
            mink.append(cur)
        x=mink[:]
        x.sort() #to sort the distances
        for j in range(len(mink)):
            y = mink.index(x[j])
            
            mink[y]=100   #change mapped values to avoid index         
            answer[j]=points[y] #map the sorted distance with the input
                  
        return answer[:k]
            

x=Solution()
# print(x.kClosest([[0,1], [1,0]], 2))
# print(x.kClosest([[3,3],[5,-1],[-2,4]], 2))
print(x.kClosest([[-2,10],[-4,-8],[10,7],[-4,-7]],
3))
