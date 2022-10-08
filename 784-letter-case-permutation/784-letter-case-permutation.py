class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letter_positions = [] #to only go through the letters in each iteration
        for i, let in enumerate(s):
            if not let.isdigit():
                letter_positions.append(i)
                
        res = [s]
        def backtrack(i, ans):
            temp = ans[i]
            ans[i] = ans[i].upper() if ans[i].islower() else ans[i].lower()            
            res.append("".join(ans))
            
            for j in letter_positions:
                if j > i:
                    backtrack(j, ans)
            ans[i] = temp
                    
        for pos in letter_positions:
            backtrack(pos, list(s))
        return res