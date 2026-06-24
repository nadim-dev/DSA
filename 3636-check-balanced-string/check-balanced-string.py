class Solution:
    def isBalanced(self, nums: str) -> bool:
        n=len(nums)
        oddSum=0
        evenSum=0
        for i in range(0,len(nums)):
            if i%2==0:
                evenSum+=int(nums[i])
            else:
                oddSum+=int(nums[i])

        if oddSum == evenSum:
            return True
        else:
            return False
            

           