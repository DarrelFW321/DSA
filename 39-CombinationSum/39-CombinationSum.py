# Last updated: 2/11/2026, 11:08:37 AM
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        #for each index, run a recursive loop

        #conditions/parameters
        #we set variables for the remainder
        #we set the index

        result = []
        paths = []

        def recurse(i, remainder):
            if remainder == 0:
                result.append(list(paths))
                return

            if remainder < 0:
                return

            if i == len (candidates):
                return
            
            paths.append(candidates[i])
            recurse (i, remainder-candidates[i])
            paths.pop()

            recurse (i +1, remainder)

        recurse(0, target)
        return result

        