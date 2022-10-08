class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def calculate(p1, p2):
            return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

        def buildgraph(points):
            neighbors = defaultdict(list)
            for i, point in enumerate(points):
                for neigh in points:
                    if points != neigh:
                        neighbors[i].append(calculate(point, neigh))
            return neighbors
            
        graph = buildgraph(points)
        res = 0
        for point in graph.keys():
            freq = Counter(graph[point])
            temp = 0
            for neigh in freq.keys():
                k = freq[neigh]
                if k >= 2: #valid boomerang formation
                    combs = k * (k - 1)
                    temp += combs
            res += temp
        
        return res


