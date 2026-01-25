class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        ans.append(nums[0])
        for i in range(1,n):
            ans.append(nums[i]+ans[i-1])
        return ans