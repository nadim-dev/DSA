class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        startPos=-1
        endPos=-1
        for i in range(len(nums)):
            if nums[i] == target:
                if startPos == -1:
                    startPos=i
                endPos=i

        return [startPos,endPos]

                
            
            
            