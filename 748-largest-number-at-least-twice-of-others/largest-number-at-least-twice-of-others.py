class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_element=nums[0]
        index=0
        
        for i in range(1,len(nums)):
            if(nums[i]>=max_element):
                max_element=nums[i]
                index=i
        for i in range(0,len(nums)):
            if(index == i):
                continue
            
            if(max_element<2*nums[i]):
              return -1
        return index