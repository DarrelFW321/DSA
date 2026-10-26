# Last updated: 10/26/2026, 1:31:36 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8from collections import deque
9class Solution:
10    def rightSideView(self, root: TreeNode | None) -> list[int]:
11        
12        if not root:
13            return []
14
15        res = []
16        queue = deque()
17
18        queue.append((root,1))
19
20        while queue:
21            # print(queue)
22            node, level = queue.popleft()
23            if node:
24                # print(node.right)
25                # print(res)
26                # print(level)
27                if len(res) < level:
28                    res.append(node.val)
29                queue.append((node.right, level+1))
30                queue.append((node.left,level + 1))
31
32
33
34        return res
35
36
37        
38
39