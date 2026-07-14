class Move_Zeoes {
    public static void moveZeroes(int[] nums) {
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
    System.out.println(l);
}
    public static void main(String[] args) {
        int nums[] = {2,5,6,1};
        moveZeroes(nums);
    }
}