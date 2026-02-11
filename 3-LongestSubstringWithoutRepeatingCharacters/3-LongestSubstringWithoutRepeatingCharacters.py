# Last updated: 2/11/2026, 11:08:51 AM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        #use left and right, where left is index 0 and right is at index 1
        #we check for duplicate characters at each window restricted by left and right

        #use a set

        #loop
        
        #if within the window, a duplicate is found, we move left to the right, until there are no duplicates

        #once there are no duplicates move right to the right



        left = 0
        right = 1
        maxLen = 0
        flag = False

        while (right <= len(s)):
            st = set()

            for ch in s[left:right]:
                if ch not in st:
                    flag = False
                    st.add(ch)
                else:
                    flag = True
                    break

            if flag:
                left+=1
            else:
                maxLen = max(maxLen, len(st))
                right+=1

        return maxLen