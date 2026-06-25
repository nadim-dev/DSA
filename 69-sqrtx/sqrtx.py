class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0:
            return x
            
        ans=1
        l=1
        h=x
        while l<=h:
            mid=(l+h)//2

            square=mid*mid
            if square > x:
                h=mid-1
            else:
                ans=mid
                l=mid+1
        return ans
