// Last updated: 2/11/2026, 11:08:48 AM
class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> table = new HashMap <Character, Integer>();
        table.put('I', 1);
        table.put('V', 5);
        table.put('X', 10);
        table.put('L', 50);
        table.put('C', 100);
        table.put('D', 500);
        table.put('M', 1000);
        int total = 0;
        for (int n = 0 ; n < s.length()-1; n++){
            if(table.get(s.charAt(n)) < table.get(s.charAt(n+1))){
                total -= table.get(s.charAt(n));
            }
            else{
                total += table.get(s.charAt(n));
            }
        }
        total+= table.get(s.charAt(s.length()-1));
        return total;
    }
}