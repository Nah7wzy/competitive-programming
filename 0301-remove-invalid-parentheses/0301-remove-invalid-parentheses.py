class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        min_op = len(s)
        def backtrack(i, temp, count, removed):
            nonlocal min_op
            if removed > min_op or count < 0:
                return False
            
            if i >= len(s):
                if count != 0:
                    return False
                
                min_op = min(min_op, removed)
                res.add(temp)
                return True
            
            if s[i] not in ('(', ')'):
                backtrack(i+1, temp + s[i], count, removed)
            else:
                backtrack(i+1, temp + s[i], count + 1 if s[i] == '(' else count - 1, removed)
                backtrack(i+1, temp, count, removed + 1)
           
            
        backtrack(0, "", 0, 0)
        return res
                
                
                
        
                
                