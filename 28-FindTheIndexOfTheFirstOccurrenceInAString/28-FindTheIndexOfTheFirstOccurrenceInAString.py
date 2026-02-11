# Last updated: 2/11/2026, 11:08:39 AM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1

        streakstart = 0
        streak = False
        j = 0  # index in needle
        i = 0

        while i < len(haystack):
            if not streak:
                if haystack[i] == needle[0]:
                    streak = True
                    streakstart = i
                    j = 1
                    if len(needle) == 1:
                        return i
                i += 1
            else:
                if haystack[i] == needle[j]:
                    j += 1
                    i += 1
                    if j == len(needle):
                        return streakstart
                else:
                    # reset and try next start position
                    i = streakstart + 1
                    streak = False

        return -1
