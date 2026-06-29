class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insertPosition=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[insertPosition]=nums[i]
                insertPosition+=1
        while insertPosition<len(nums):
            nums[insertPosition]=0
            insertPosition+=1
        return nums

        