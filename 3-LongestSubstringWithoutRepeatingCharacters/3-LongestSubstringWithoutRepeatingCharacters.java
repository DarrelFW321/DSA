// Last updated: 2/11/2026, 11:08:53 AM
class Solution {
    public int lengthOfLongestSubstring(String s) {

        int windowStart = 0;
        int max = 0;
        HashSet<Character> set = new HashSet<Character>();

        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++){
            char temp = s.charAt(windowEnd);
            if(!set.contains(temp))
            {
                set.add(temp);
            }
            else{
                while(set.contains(temp)){
                    set.remove(s.charAt(windowStart));
                    windowStart++;
                }
                set.add(temp);
            }
            if (max<set.size()){
                    max = set.size();
                }
        }
        return max;    
    }
}