class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        prefix=1
        suffix=1
        for i in range(0,len(nums)):
            prefix=prefix*nums[i]
            suffix=suffix*nums[len(nums)-1-i]
            max_prod=max(max_prod,max(prefix,suffix))

            if prefix==0:
                prefix=1
            if suffix ==0:
                suffix=1
            
             


        return max_prod