
class Solution {
    public int[] twoSum(int[] nums, int target) {
        return this.sol(nums, target);
    }
    
    public int[] sol1(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i=0; i < nums.length; i++){
            
            int comp = target - nums[i];
            
            if (map.containsKey(comp)) {
                return new int[] {map.get(comp), i};
            }
            map.put(nums[i], i);
        }
        
        return new int[] {};
    }
    
    public int[] sol(int[] nums, int target) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i=0; i < nums.length; i++){
            
            int n = nums[i];
            int diff = target - n;
            
            if (map.containsKey(diff)){
                return new int[]{map.get(diff), i};
            }
            else {
                map.put(n, i);
            }   
        }
        
        return new int[]{};
    }
}