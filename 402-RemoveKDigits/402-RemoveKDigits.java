// Last updated: 2/11/2026, 11:08:20 AM
class Solution {
    public String   removeKdigits(String num, int k){
        Stack <Character> stack = new Stack<Character> ();

        for (char digit : num.toCharArray()) {
            while (!stack.isEmpty() && k > 0 && stack.peek() > digit) {
                stack.pop();
                k--;
            }
            stack.push(digit);
        }
        
        // Remove remaining k digits from the end of the stack
        while (k > 0 && !stack.isEmpty()) {
            stack.pop();
            k--;
        }
        
        StringBuilder obj = new StringBuilder ();
        while(!stack.isEmpty()){
           obj.append(stack.pop());
        }
   
        obj.reverse();
        while (obj.length() > 0 && obj.charAt(0) == '0'){
               obj.deleteCharAt(0);
        }

        if(obj.length() ==0){
            return "0";
        }  

        return obj.toString();
    }
}