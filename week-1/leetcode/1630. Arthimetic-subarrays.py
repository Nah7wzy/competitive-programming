class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        def check(x):
            x.sort()
            dif=abs(x[1]-x[0])
            for j in range(1,len(x)-1):
                if abs(x[j+1]-x[j])!=dif:
                    return False
                else:
                    pass
            return True
        answer=[]
        for i in range(len(l)):
            answer.append(check(nums[l[i]:r[i]+1]))
        return answer

x=Solution()
print(x.checkArithmeticSubarrays([4,6,5,9,3,7],
[0,0,2],
[2,3,5]))