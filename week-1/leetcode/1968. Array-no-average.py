# if (nums[i-1]+nums[i+1])/2==nums[i]:
#                 nums[i+1],nums[-1]=nums[-1],nums[i+1]
def rearrangeArray(nums):
    odd=[]
    even=[]
    for i in nums:
        even.append(i) if i%2==0 else odd.append(i)
    
    return odd

print(rearrangeArray([1,2,3,4,5]))