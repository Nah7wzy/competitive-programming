class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb = {'2': {'a','b','c'}, '3': {'d','e','f'}, '4': {'g','h','i'}, '5': {'j','k','l'}, '6': {'m','n','o'}, '7': {'p','q','r','s'}, '8': {'t','u','v'}, '9': {'w','x','y','z'}}
        res = []
        ans = []
        def dfs(i, res):
            nonlocal ans
            if i >= len(digits):
                if i > 0:
                    ans.append(''.join(res))
                return
            
            for letter in comb[digits[i]]:
                res.append(letter)
                dfs(i+1, res)
                res.pop()
                
        dfs(0, res)
        return ans