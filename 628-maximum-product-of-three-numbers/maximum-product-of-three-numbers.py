class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)-1
        case_1=nums[n]* nums[n-1] * nums[n-2]
        case_2=nums[0]*nums[1]*nums[n]
        return max(case_1,case_2)