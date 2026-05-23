# Last updated: 5/23/2026, 12:38:34 AM
1class LRUCache:
2    class Node:
3        def __init__ (self, key:int, data: int):
4            self.key = key
5            self.data = data
6            self.next = None
7            self.prev = None
8
9    def __init__(self, capacity: int):
10        self.storage = {} #key -> pointer to linked list
11
12        self.tail = None
13        self.head = None
14
15        self.capacity = capacity
16        self.len = 0
17
18    def get(self, key: int) -> int:
19        if (key in self.storage):
20            self.put(key, self.storage[key].data)
21            return self.storage[key].data
22        else:
23            return  -1
24
25
26    def put(self, key: int, value: int) -> None:
27        if (key in self.storage):
28            old_node = self.storage[key]
29            old_node.data = value
30
31            if old_node is self.tail:
32                if old_node is self.head:
33                    return
34
35                new_tail = self.tail.next
36                new_tail.prev = None
37                self.tail = new_tail
38
39                old_node.prev = self.head
40                old_node.next = None
41                self.head.next = old_node
42                self.head = old_node
43                return
44
45            if old_node is self.head:
46                return
47
48            old_prev = old_node.prev
49            old_next = old_node.next
50
51            old_prev.next = old_next
52            old_next.prev = old_prev
53
54            old_node.prev = self.head
55            old_node.next = None
56            self.head.next = old_node
57            self.head = old_node
58        else:
59            new_node = self.Node(key, value)
60            if not self.tail:
61                self.tail = new_node
62                self.head = new_node
63                self.len+=1
64                self.storage[key] = new_node
65                return
66            
67            if self.len < self.capacity:
68                self.head.next = new_node
69                new_node.prev = self.head
70                self.head = new_node
71                self.len+=1
72                self.storage[key] = new_node
73                return
74            
75            del self.storage[self.tail.key]
76
77            # If capacity is 1, replace the only node
78            if self.capacity == 1:
79                self.tail = new_node
80                self.head = new_node
81                self.storage[key] = new_node
82                return
83
84            self.storage[key] = new_node
85
86            new_tail = self.tail.next
87            new_tail.prev = None
88            self.tail = new_tail
89
90            self.head.next = new_node
91            new_node.prev = self.head
92            self.head = new_node
93
94        
95
96
97# Your LRUCache object will be instantiated and called as such:
98# obj = LRUCache(capacity)
99# param_1 = obj.get(key)
100# obj.put(key,value)