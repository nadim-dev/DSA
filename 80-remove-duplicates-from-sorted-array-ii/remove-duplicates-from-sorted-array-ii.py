class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)==2):
            return len(nums)
        start=1

        for j in range(2,len(nums)):
            if(nums[start-1]!=nums[j]):
                start=start+1
                nums[start]=nums[j]

        return start+1