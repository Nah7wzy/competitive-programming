class Solution:
    def pancakeSort(self, arr):
        answer=[]
        for i in range(len(arr), 0, -1):
            # print(i)
            y=max(arr[:i])
            
            k=arr.index(y)
            answer.append(k)
            temp=arr[:(arr.index(y)+1)]
            temp.reverse()
            arr[:(arr.index(y)+1)]=temp
            temp=arr[:i]
            temp.reverse()
            arr[:i]=temp
            # arr.reverse()
            # answer.append(arr.index(y))
            # print(arr)
        return answer

x=Solution()
print(x.pancakeSort([3,2,4,1]))