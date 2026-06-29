class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_consicutive_count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                count+=1
            else:
                max_consicutive_count=max(max_consicutive_count,count) 
                count=0    

        return max(max_consicutive_count,count)