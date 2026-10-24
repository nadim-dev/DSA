class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        low=0
        high=0
        n=len(nums)
        result=float("inf")
        sum=nums[low]

        while high<n:
            if sum>=target:
                lenght=high-low+1
                result=min(result,lenght)
                low=low+1
                sum=sum-nums[low-1]
            else:
                high=high+1
                if high>=n:
                    break
                sum=sum+nums[high]
        if result == inf:
            return 0
        else:
            return result