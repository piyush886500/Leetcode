class Solution {
    public void moveZeroes(int[] nums) {
        int l = 0;
        int size = nums.length;
        for(int r =0;r<size;r++){
            if(nums[r]!=0){
                int temp = nums[l];
                nums[l]=nums[r];
                nums[r]=temp;
                l++;
            }    
    }
}
}