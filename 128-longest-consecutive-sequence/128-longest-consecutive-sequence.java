class Solution {
    public int longestConsecutive(int[] nums) {
        
        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < nums.length; i++){
            set.add(nums[i]);
        }
        
        int res = 0;
        for (int i = 0; i < nums.length; i++){
            if (!set.contains(nums[i]-1)){
                int current = nums[i];
                int max = 0;
                while (set.contains(current + 1)){
                    max++;
                    current++;
                }
                res = Math.max(res, max+1);
            }   
        }
        
        return res;
    }
}