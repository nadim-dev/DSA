class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        min=nums[0]
        while low<=high:
            mid=(low+high)//2
            if nums[low] == nums[high] == nums[mid]:
                if nums[low]<min:
                    min=nums[low]
                low+=1
                high-=1
                continue
            #left part is sorted
            if low>high:
                break
            if nums[low]<=nums[mid]:
                if nums[low]<min:
                    min=nums[low]
                low=mid+1
            else:
                if nums[mid]<min:
                   min=nums[mid]
                high=mid-1
        return min
                 