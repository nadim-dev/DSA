class Solution:
    def lowerbound(self,nums,target):
        lb=-1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    def Upperbound(self,nums,target):
        ub=len(nums)
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb=self.lowerbound(nums,target)
        if lb == -1 or nums[lb]!=target:
            return [-1,-1]
        ub=self.Upperbound(nums,target)
        return [lb,ub-1]

                
            
            
            