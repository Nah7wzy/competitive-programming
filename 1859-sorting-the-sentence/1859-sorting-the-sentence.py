class Solution:
    def sortSentence(self, s: str) -> str:
        words = set()
        temp = ""
        for i in s:
            if i.isdigit():
                words.add((i, temp))
                temp = ""
            elif i != " ":
                temp += i
                
        order = sorted(words)
        res = ""
        for x in order:
            res = res + " " + x[1]
            
        return res.strip()
                
                