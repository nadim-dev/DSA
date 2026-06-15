class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        if(len(nums)==1):
            return nums
        while(i<=j):
            if(nums[i]%2==0):
                i=i+1
            elif(nums[i]%2!=0 and nums[j]%2==0):
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j-=1
            else:
                j=j-1
        return nums