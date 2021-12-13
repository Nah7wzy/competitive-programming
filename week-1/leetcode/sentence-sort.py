class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        new_sent=[0]*len(s)
        for i in s:
            pos =i[-1]
            x=len(i)
            new_sent[(int(pos)-1)]=i[:x-1]
        ns=""
        for j in range(len(new_sent)):
            ns=ns+new_sent[j]+("" if j == len(new_sent)-1 else " ")
        
        print(ns)
        return ns