# Last updated: 2/11/2026, 11:08:25 AM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mp_s = {}
        mp_t = {}

        for ch in s:
            mp_s[ch] = mp_s.get(ch,0) + 1

        for ch in t:
            mp_t[ch] = mp_t.get(ch,0) + 1

        for key,value in mp_s.items():
            if mp_s[key] != mp_t.get(key,0):
                return False

        return True
        