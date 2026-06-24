class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        startPos=-1
        isStartPosExist=False
        count=0
        for i in range(len(nums)):
            if nums[i] == target:
                if not isStartPosExist:
                    isStartPosExist=True
                    startPos=i
                else :    
                    count+=1

        return [startPos,startPos+count]

                
            
            
            