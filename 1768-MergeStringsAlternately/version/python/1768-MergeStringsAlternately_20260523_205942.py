# Last updated: 5/23/2026, 8:59:42 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        i = 0
4        j = 0
5
6        res = ""
7
8        while (i < len(word1) and j < len(word2)):
9            res+= word1[i]
10            res+= word2[j]
11            i+=1
12            j+=1
13
14        if (len (word1) > len(word2)):
15            res+= word1[i:]
16            return res
17
18        if (len(word2) > len(word1)):
19            res+= word2[j:]
20            return res
21
22        return res