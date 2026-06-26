class Solution {
    public boolean isPalindrome(int x) {
        if(x<0 || (x % 10 == 0 && x != 0)) return false;
        int res = 0;
        int n = x;
        while (x>res) {
            int digit = x % 10;
            res = res * 10 + digit;
            x /= 10;   
        }
        
        return x==res || x==res/10;
    }
}
