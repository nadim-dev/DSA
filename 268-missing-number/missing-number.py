class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0

        for i in range(len(nums)):
            sum+=nums[i]
        n=len(nums)
        n_natural_number_sum=(n*(n+1))//2
        return n_natural_number_sum-sum