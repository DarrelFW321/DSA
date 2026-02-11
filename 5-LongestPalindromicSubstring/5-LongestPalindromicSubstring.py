# Last updated: 2/11/2026, 11:08:48 AM
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = ""


        #find odd palindromes
        for i in range(len(s)):
            left = i
            right = i+1

            while (left >=0 and right <= len(s)):
                if (s[left] != s[right-1]):
                    break
                if len(result) < len(s[left:right]):
                    result = s[left:right]
                left -= 1
                right +=1

        #find even palindromes
        for i in range(len(s)):
            left = i
            right = i

            while (left >=0 and right <= len(s)):
                if (s[left] != s[right-1]):
                    break
                if len(result) < len(s[left:right]):
                    result = s[left:right]
                left -= 1
                right +=1

        return result
        