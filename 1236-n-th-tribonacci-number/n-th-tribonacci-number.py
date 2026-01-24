class Solution:
    def tribonacci(self, n: int) -> int:
        seen={}
        def solve(n):
            if(n==0 or n==1):
                return n
            if(n==2):
                return n-1
            if n in seen:
              return seen[n]

            seen[n]=solve(n-1)+solve(n-2)+solve(n-3)
            return seen[n]

        return solve(n)