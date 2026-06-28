class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isdecreasing=True
        isincreasing=True
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                isdecreasing=False
            elif nums[i]>nums[i+1]:
                isincreasing=False
        if isdecreasing or isincreasing:
            return True
        else:
            return False 