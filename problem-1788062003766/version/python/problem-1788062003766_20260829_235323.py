# Last updated: 8/29/2026, 11:53:23 PM
1class Solution:
2    def minOperations(self, nums: list[int], sum: int) -> int:
3
4        
5        
6
7        def check(nums, target):
8            dp = [False] * (target+1)
9            dp[0] = True
10
11            for x in nums:
12                for s in range(target,x-1,-1):
13                    if dp[s-x]:
14                        dp[s] = True
15
16            return dp[target]
17
18        def getoptions(x, target):
19            options = []
20            options.append((x,0))
21
22            value = x*2
23            cost = 1
24
25            while (value <= target):
26                options.append((value,cost))
27                cost+=1
28                value*=2
29
30            value = x//2
31            cost =1 
32
33            while value > 0:
34                options.append((value,cost))
35                cost +=1
36                value= value//2
37
38            return options
39
40            
41
42        def check2(nums, target):
43            dp = [float('inf')] * (target+1)
44            dp[0] = 0
45
46            for x in nums:
47                options = getoptions(x,sum)
48
49                newdp = dp[:]
50                for value,cost in options:
51                    for s in range(target+1):
52                        if dp[s] != float('inf') and s + value <= target:
53                            newdp[s+value] = min(cost + dp[s], newdp[s+value])
54
55                dp = newdp
56
57
58            if dp[target] == float('inf'):
59                return -1
60            return dp[target]
61
62        
63
64        return check2(nums,sum)
65                