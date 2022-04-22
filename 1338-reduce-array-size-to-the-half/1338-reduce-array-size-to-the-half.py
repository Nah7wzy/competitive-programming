class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq={}
        answer = 0
        n = len(arr)/2 #to know when half is passed
        for i in arr:
            if i not in freq:
                freq[i]=0
            freq[i]+=1
            
        arr = sorted(freq.values(),reverse = True) # to start from higher values
        
        count = 0 #keep count of frequencies
        for i in arr:
            count += i
            answer += 1
            if count >= n:
                break
                
        return answer