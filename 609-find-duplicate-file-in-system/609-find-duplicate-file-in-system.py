class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for path in paths:
            directory, *files = path.split() #split using space, then unpack files into a list, use the first as directory
            
            for file in files:
                name, content = file.split('(')
                d[content].append(directory + '/' + name) #default value is intialized to list so append full name to the list
                
        res = [duplicate for duplicate in d.values() if len(duplicate) > 1]
        return res