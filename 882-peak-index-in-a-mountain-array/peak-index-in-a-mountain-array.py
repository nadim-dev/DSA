class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low=0
        high=len(arr)-1
        peak=0
        while low<high:
            mid=(low+high)//2

            #check which part is sorted
            if arr[mid]<arr[mid+1]:
                low=mid+1
            else:
                high=mid
        return low
            
        



            