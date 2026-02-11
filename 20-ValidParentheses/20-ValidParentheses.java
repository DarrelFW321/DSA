// Last updated: 2/11/2026, 11:08:41 AM
class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> table = new HashMap<Character, Character>();
        table.put('{', '}');
        table.put('(', ')');
        table.put('[', ']');
        Stack<Character> stack = new Stack <Character>();
        for (int n = 0; n< s.length(); n++){
            if (stack.isEmpty()){
                stack.push(s.charAt(n));
            }
            else{
                if (table.get(stack.peek()) != null){
                    if(s.charAt(n) == table.get(stack.peek())){
                       stack.pop();
                    }
                    else{
                       stack.push(s.charAt(n));
                    }
                }
                else{
                    stack.push(s.charAt(n));
                }
            }         
        }
        if (stack.isEmpty()){
            return true;
        }
        return false;
    }
}