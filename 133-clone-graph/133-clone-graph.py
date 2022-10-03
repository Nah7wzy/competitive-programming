"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node:
            d = {node: Node(node.val)} #to store clone of nodes
            q = deque([node])
            #bfs
            while q:
                curr = q.popleft()
                for neighbor in curr.neighbors:
                    if neighbor not in d:
                        d[neighbor] = Node(neighbor.val)
                        q.append(neighbor)
                    #append neighbors for node copy of current node
                    d[curr].neighbors.append(d[neighbor])

            return d[node] #copy of starting node