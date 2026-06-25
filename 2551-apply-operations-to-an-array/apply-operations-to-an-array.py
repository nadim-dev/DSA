class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
        k=0    
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[k],nums[i]=nums[i],nums[k]
                k+=1

        return nums
                   

