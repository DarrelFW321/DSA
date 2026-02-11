# Last updated: 2/11/2026, 11:08:45 AM
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        values = {'I': 1, 'V':5, 'X':10,'L':50,'C':100,'D':500, 'M':1000}
    
        if len(s) == 1:
            return values[s]

        left = 0

        total = 0

        while (left < len(s)):
            print("left ", s[left])
            if left+1<len(s):
                if values[s[left]] < values[s[left+1]]:
                    total+=values[s[left+1]]-values[s[left]]
                    left+=2
                else:
                    total+=values[s[left]]
                    left+=1
            else:
                total+=values[s[left]]
                left+=1

        return total

        