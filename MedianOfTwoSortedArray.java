class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len = nums1.length+nums2.length;
        int n1=nums1.length;
        int n2 = nums2.length;
        int[] merged = new int[len];
        int i=0,j=0,k=0;
        while(i<n1 && j<n2){
            if(nums1[i]<nums2[j]){
                merged[k]=nums1[i];
                i++;
                k++;
            }
            else{
                merged[k]=nums2[j];
                j++;
                k++;
            }
        }
        while(i<n1) merged[k++] = nums1[i++];
        while(j<n2) merged[k++] = nums2[j++];
        
        if(len%2==0) {
            double d = (merged[len/2-1]+merged[len/2])/2.0;
                return d;
        }
        double d = merged[len/2];
        return d;
    }
}