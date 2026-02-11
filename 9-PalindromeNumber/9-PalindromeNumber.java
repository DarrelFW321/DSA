// Last updated: 2/11/2026, 11:08:49 AM
class Solution {
    public boolean isPalindrome(int x) {
        if (x<0){
            return false;
        }
        StringBuilder z = new StringBuilder(String.valueOf(x));
        if (z.toString().equals(z.reverse().toString())){
            return true;
        }
        return false;
    }
}