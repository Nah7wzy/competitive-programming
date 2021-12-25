class Solution:
    def isValid(self, s: str) -> bool:
        opench=['(', '{', '[']
        closech=[')', '}', ']']
        unclosed=[]
        for i in s:
            if i in opench:
                x=opench.index(i)
                unclosed.append(x)
               
            elif i in closech:
                y=closech.index(i)
                if y in unclosed:
                    print(unclosed)
                    if y==unclosed[-1]:
                        unclosed.pop()
                    else: 
                        return False
                else:
                    return False
        if unclosed==[]:
            return True
        else:
            return False

x=Solution()
print(x.isValid("[([]])"))