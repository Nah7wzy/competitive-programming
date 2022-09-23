class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        family = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(beginWord)):
                pattern = word[:i] + '*' + word[i+1:]
                family[pattern].append(word) 
              
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                if x == endWord:
                    return res
                
                for j in range(len(x)):
                    pattern = x[:j] + '*' + x[j+1:]
                    
                    for neighbor in family[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)                            
            res += 1
            
        return 0
        