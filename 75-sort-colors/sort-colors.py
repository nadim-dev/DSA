class Solution:
    def sortColors(self, nums: List[int]) -> None:
       left=0
       rigth=len(nums)-1
       i=0
       while(i<=rigth):
        if nums[i] == 0:
            nums[i],nums[left]=nums[left],nums[i]
            left+=1
            i=i+1
        elif nums[i]==2:
            nums[i],nums[rigth]=nums[rigth],nums[i]
            rigth-=1
        else:
            i+=1
        