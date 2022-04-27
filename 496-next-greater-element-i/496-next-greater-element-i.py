class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp=[] #keep track of index of nums1 in nums 2
        result=[]
        for i in range(len(nums1)):
            temp.append(nums2.index(nums1[i]))
                
        for i in range(len(temp)):
            index=temp[i] #to start next loop from its index
            value = nums1[i]
            count=0 #check if it has been found or none exist
            for j in range(index+1,len(nums2)):
                if nums2[j] > value:
                    count+=1
                    result.append(nums2[j])
                    break;
                    
            if count==0:
                result.append(-1)
        
        return result