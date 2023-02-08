class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i, (A, B) in enumerate(equations):
            if A in graph:
                graph[A][B] = values[i]
            else:
                graph[A] = {B: values[i]}
            if B in graph:
                graph[B][A] = 1/values[i]
            else:
                graph[B] = {A: 1/values[i]}

        def dfs(A, B, visited):
            if A not in graph or B not in graph:
                return -1.0
            if B in graph[A]:
                return graph[A][B]
            visited.add(A)
            for node in graph[A]:
                if node not in visited:
                    result = dfs(node, B, visited)
                    if result != -1.0:
                        return result * graph[A][node]
            return -1.0

        res = []
        for C, D in queries:
            visited = set()
            res.append(dfs(C, D, visited))
        return res