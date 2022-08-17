class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformation = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = set()
        count = 0
        for word in words:
            temp = ""
            for letter in word:
                # print(ord('a'))
                temp += transformation[ord(letter) -97]
            if temp not in res:
                count += 1
                res.add(temp)
            
        return count