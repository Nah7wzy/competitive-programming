class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for u, v in adjacentPairs:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()
        res = []

        def dfs(node, prev=None):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    if prev is None or neighbor != prev:
                        res.append(neighbor)
                        dfs(neighbor, node)
                    else:
                        res.insert(0, neighbor)
                        dfs(neighbor, node)
                        
        for key in adj_list:
            if len(adj_list[key]) == 1:
                start = key
                break
                
        dfs(start)
        res.insert(0, start)
        return res