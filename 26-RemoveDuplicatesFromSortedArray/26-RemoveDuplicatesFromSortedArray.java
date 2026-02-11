// Last updated: 2/11/2026, 11:08:40 AM
class Solution {
    public int removeDuplicates(int[] nums) {
        int temp = -101;
        int k = 0;
        int z = 0;
        for (int n = 0; n < nums.length; n++){
            if (nums[n] > temp){
                temp = nums[n];
                nums[z] = temp;
                z++;
                k++;
             }
        }
        return k;
    }
}