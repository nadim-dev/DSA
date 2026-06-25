class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        
        start=k-1
        for j in range(start+1,len(nums)):
            if nums[start-(k-1)]!=nums[j]:
                start+=1
                nums[start]=nums[j]
        
        return nums[:start+1]

            