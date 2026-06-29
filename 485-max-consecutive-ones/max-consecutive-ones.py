class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_consicutive_count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                count+=1
                max_consicutive_count=max(max_consicutive_count,count)
            else:
                count=0    

        return max_consicutive_count