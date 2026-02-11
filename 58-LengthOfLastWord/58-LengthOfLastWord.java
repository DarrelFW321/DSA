// Last updated: 2/11/2026, 11:08:34 AM
class Solution {
    public int lengthOfLastWord(String s) {
        StringBuilder obj = new StringBuilder (s);
        obj.reverse();
        int x = obj.indexOf(" ");
        if (x == -1){
            return s.length();
        }
        if(obj.charAt(0) != ' '){
            return x;
        }
        while (true){
            if (obj.indexOf(" ", x+1) == -1){
                return s.length()-1-x;
            } 
            if (obj.indexOf(" ", x+1) == x+1){
                x++;
                continue;
            }
            return obj.indexOf(" ", x+1)-x-1;
        }
    }
}