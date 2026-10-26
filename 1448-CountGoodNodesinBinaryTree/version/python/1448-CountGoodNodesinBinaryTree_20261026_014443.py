# Last updated: 10/26/2026, 1:44:43 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def goodNodes(self, root: TreeNode) -> int:
10        
11        if not root:
12            return 0
13
14        res  = 0
15
16        queue = deque()
17        queue.append((root, None))
18
19        while queue:
20            node, currmax = queue.popleft()
21            if node:
22                if currmax is None or currmax <= node.val :
23                    res+=1
24                    currmax = node.val
25
26                queue.append((node.left, currmax))
27                queue.append((node.right,currmax))
28
29        return res
30
31