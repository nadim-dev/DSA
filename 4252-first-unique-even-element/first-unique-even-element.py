class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        dict={}
        for i in range(0,len(nums)):
             if nums[i] not in dict:
                dict[nums[i]]=1
             else:
                dict[nums[i]]+=1    

        for key,values in dict.items():
            if key%2 ==0 and values ==1:
                return key
        return -1          