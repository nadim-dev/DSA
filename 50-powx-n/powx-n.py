class Solution:
    def pow(self,x,n):
        #base case
        if (n == 0):
            return 1
        #recursive case
        a=self.pow(x,n//2)
        if (n%2 == 0):
            return a*a
        else:
            return a*a*x
    def myPow(self, x: float, n: int) -> float:
        if (n>=0):
            return self.pow(x,n)
        else:
            return 1/self.pow(x,n*(-1))