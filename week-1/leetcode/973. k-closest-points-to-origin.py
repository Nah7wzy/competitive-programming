class Solution:
    def calculate_d(self, arr):
        return (((arr[0])**2) + ((arr[1])**2))**0.5
    def kClosest(self, points, k):
        min= self.calculate_d(points[0])
        answer=points[:]
        mink=[]
        for i in points:
            cur = self.calculate_d(i)
            mink.append(cur)
        x=mink[:]
        x.sort()
        print(mink)
        for j in range(len(mink)):
            y = mink.index(x[j])
            
            mink[j]=100
            
            print(y)
            
            answer[j]=points[y]
            
        
                
        return answer[:k]

x=Solution()
print(x.kClosest([[3,3],[5,-1],[-2,4]], 2))