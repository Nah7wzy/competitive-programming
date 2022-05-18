class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        i=j=0
        res = 0
        for j,fruit in enumerate(fruits):
            if fruit not in d:
                d[fruit] = 1
            else:
                d[fruit]+=1
            while len(d)>2 and i<j:
                d[fruits[i]]-=1
                if d[fruits[i]] == 0:
                    d.pop(fruits[i],None)
                i+=1
            res = max(res,sum(d.values()))
        return res