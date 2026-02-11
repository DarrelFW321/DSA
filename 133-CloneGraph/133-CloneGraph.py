# Last updated: 2/11/2026, 11:08:31 AM
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        visited = set()

        # Collect all nodes via DFS
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for neighbor in n.neighbors:
                dfs(neighbor)

        dfs(node)

        # Map original node object -> cloned node
        nodes_copy = {}

        for n in visited:
            newNode = Node(n.val)
            nodes_copy[n] = newNode

        for n in nodes_copy:
            for n_neighbor in n.neighbors:
                nodes_copy[n].neighbors.append(nodes_copy[n_neighbor])

        return nodes_copy[node]