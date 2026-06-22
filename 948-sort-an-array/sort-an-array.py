class Solution:


    def merge(self,nums,l,mid,r):
        a=[]
        b=[]
        for i in range(l,mid+1):
            a.append(nums[i])
        
        for i in range(mid+1,r+1):
            b.append(nums[i])
        i=0
        j=0
        k=l

        while(k<=r):
            if i==len(a):
                nums[k]=b[j]
                k+=1
                j+=1
            
            elif j==len(b):
                nums[k]=a[i]
                k+=1
                i+=1
            
            elif a[i]<b[j]:
                nums[k]=a[i]
                i=i+1
                k=k+1
            else:
                nums[k]=b[j]
                j=j+1
                k=k+1
            



    def mergeSort(self,nums,l,r):
        if l>=r:
            return 
        mid=(l+r)//2
        self.mergeSort(nums,l,mid)
        self.mergeSort(nums,mid+1,r)
        self.merge(nums,l,mid,r)




    def sortArray(self, nums: List[int]) -> List[int]:
         self.mergeSort(nums,0,len(nums)-1)
         return nums