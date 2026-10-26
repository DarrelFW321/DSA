# Last updated: 10/26/2026, 1:30:27 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: TreeNode | None) -> list[int]:
9        
10        if not root:
11            return []
12
13        res = []
14        queue = []
15
16        queue.append((root,1))
17
18        while queue:
19            # print(queue)
20            node, level = queue.pop()
21            if node:
22                print(node.right)
23                # print(res)
24                # print(level)
25                if len(res) < level:
26                    res.append(node.val)
27
28                queue.append((node.left,level + 1))
29                queue.append((node.right, level+1))
30
31
32        return res
33
34
35        
36
37