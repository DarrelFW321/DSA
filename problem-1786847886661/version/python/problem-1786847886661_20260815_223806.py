# Last updated: 8/15/2026, 10:38:06 PM
1class Solution:
2    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
3
4        min = None
5        res = -1
6
7        for i,v in enumerate(drones):
8            manhattan = abs(v[0] - target[0]) + abs(v[1]-target[1])
9            # print("manhattan: ", manhattan)
10            # print("range: ", v[2])
11            # print("i : ", i)
12            if manhattan <= v[2]:
13                if min is None or manhattan < min:
14                    min = manhattan
15                    res = i
16
17        print(res)
18        return res