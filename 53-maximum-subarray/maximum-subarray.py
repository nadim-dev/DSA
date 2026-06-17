class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currentsum=0
        for i in range(0,len(nums)):
            currentsum=currentsum+nums[i]
            if(maxsum<currentsum):
                maxsum=currentsum
            if(currentsum<0):
                currentsum=0
        return maxsum