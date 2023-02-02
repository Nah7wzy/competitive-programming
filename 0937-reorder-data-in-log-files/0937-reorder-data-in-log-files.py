class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        res = []
        
        for log in logs:
            cur = log.split(' ')
            
            if cur[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        srtltr = sorted(letters, key=lambda x: (x.split()[1:], x.split()[0]))
        res = srtltr + digits
        return res