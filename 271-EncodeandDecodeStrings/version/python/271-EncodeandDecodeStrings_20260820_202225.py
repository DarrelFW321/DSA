# Last updated: 8/20/2026, 8:22:25 PM
1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        res = ""
4
5        for s in strs:
6            res += str(len(s)) + "#" + s
7
8        return res
9
10    def decode(self, s: str) -> List[str]:
11        res = []
12        i = 0
13
14        while i < len(s):
15            j = i
16
17            while s[j] != "#":
18                j += 1
19
20            length = int(s[i:j])
21
22            word_start = j + 1
23            word_end = word_start + length
24
25            res.append(s[word_start:word_end])
26
27            i = word_end
28
29        return res