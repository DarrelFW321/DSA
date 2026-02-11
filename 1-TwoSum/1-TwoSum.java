// Last updated: 2/11/2026, 11:08:57 AM
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target){
        int[] answer = new int[2];
        HashMap <Integer, Integer> map = new HashMap<Integer, Integer>(nums.length);
        for (int i = 0; i < nums.length; i++){
            map.put (target-nums[i], i);
        }
        for (int x = 0; x < nums.length; x++) {
            if (map.containsKey(nums[x]) && x != map.get(nums[x])){
                answer[0] = x;
                answer[1] = map.get(nums[x]);
            }
        }    
        return answer;
    }
}