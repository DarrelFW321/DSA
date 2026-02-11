# Last updated: 2/11/2026, 11:08:16 AM
class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        currIndex = 0
        maxLen = 0
        initialindex = 0
        seen = set()

        while (currIndex <len(word)):
            for ch in seen:
                if word[currIndex] < ch:
                    seen = set()
                    initialindex = currIndex
                    break
            seen.add(word[currIndex])

            if len(seen) == 5:
                maxLen = max(maxLen, currIndex-initialindex+1)
            
            currIndex+=1

        return maxLen
                    




        
