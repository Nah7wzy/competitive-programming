class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = float('inf')
        children = [0] * k #keep track of received cookies
        
        def dstb(bag):
            nonlocal res, children
            if bag == len(cookies):
                res = min(res, max(children))  #update with max after all bags distributed
                return
            
            if max(children) >= res: #if max cookies child already greater than last best solution no need to go further
                return
            
            for i in range(k): #branch out the candy to each child possibility
                children[i] += cookies[bag]
                dstb(bag + 1) #branch with the next bag
                children[i] -= cookies[bag] #remove on return for other branches to perform on the variable correctly
                
        dstb(0)
        return res