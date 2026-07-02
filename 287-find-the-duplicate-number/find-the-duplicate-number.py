class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
            
        my_set=set()
        for i in range(len(nums)):
            if nums[i] in my_set:
               return nums[i]
            else:
                 my_set.add(nums[i])
        return -1