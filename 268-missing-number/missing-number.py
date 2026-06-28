class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            if i>len(nums)-1:
                return i
            if i<=len(nums)-1 and i!=nums[i]:
                return i
