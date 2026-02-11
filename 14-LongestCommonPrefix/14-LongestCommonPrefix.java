// Last updated: 2/11/2026, 11:08:43 AM
class Solution {
    public String longestCommonPrefix(String[] strs) {

        boolean flag = true;
        String prefix = new String("");
        int smallestLength = -1;
        for (int n = 0; n < strs.length; n++){
            if (smallestLength == -1 || smallestLength > strs[n].length()){
                smallestLength = strs[n].length();
            }
        }
        if (smallestLength == 0){
            return "";
        }
        for (int index = 0; index <smallestLength; index++){
            for (int n = 0; n< strs.length-1; n++){
                if (strs[n].charAt(index) != strs[n+1].charAt(index)){
                    flag = false;
                    break;
                }
            }
            if (!flag){
                break;
            }
            prefix += strs[0].charAt(index);
        }
        return prefix;
    }
}