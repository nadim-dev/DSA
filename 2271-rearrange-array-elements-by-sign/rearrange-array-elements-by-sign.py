class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in range(0,len(nums)):
            if(nums[i]>0):
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        i=0
        while(2*i<len(nums)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
            i+=1
        
      
        return nums
        