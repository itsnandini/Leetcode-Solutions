class Solution {
    public boolean isPalindrome(int x) {
        boolean flag = true;
        if (x<0)
            flag = false;
        else
        {
            int rev=0;
            int n=x;
            while(n!=0)
            {
                int d=n%10;
                rev = rev*10 + d;
                n/=10;
            }
            if (rev!=x)
                flag =false;
            else 
                flag=true;
        }
        return flag;
    }
}
