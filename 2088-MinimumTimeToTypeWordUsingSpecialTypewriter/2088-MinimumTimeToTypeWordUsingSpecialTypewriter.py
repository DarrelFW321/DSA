# Last updated: 2/11/2026, 11:08:15 AM
class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        #represent characters in circle as array length of 26

        # loop through characters:
        #     find minimum movement
        #     output as array

        # loop through the array:
        #     add 1 for each movement
        #     add 1 for each 
        
        movement_arr = []
        index = 0 
        for char in word:
            difference = ord(char)-(ord('a')+index)
            if difference > 13:
                movement = -26+difference
            elif difference < -13:
                movement = 26 + difference
            else:
                movement = difference
            index = ord(char)-ord('a')

            movement_arr.append(movement)
        
        print(movement_arr)

        second =0
        position =0
        for movement in movement_arr:
            position +=movement
            if position < 0:
                position +=26

            if movement < 0:
                second-=movement
            else:
                second+=movement
            
            second+=1

        return second
    
print (Solution().minTimeToType("abc"))