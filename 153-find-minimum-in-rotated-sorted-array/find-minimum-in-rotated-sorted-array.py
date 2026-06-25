class Solution:
    def findMin(self, nums: List[int]) -> int:
        min=nums[0]
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            #if left part is sorted
            if nums[low]<=nums[mid]:
                if nums[low]<min:
                    min=nums[low]
                low=mid+1
            else:
                if nums[mid]<min:
                    min=nums[mid]
                high=mid-1

               
        return min
               