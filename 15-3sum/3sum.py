class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_arr=sorted(nums)
        ans=[]
        n=len(sorted_arr)
        for i in range(0,n-2):
            if  i>0 and sorted_arr[i] == sorted_arr[i-1]:
                continue
            left=i+1
            right=n-1
            target=-1*sorted_arr[i]
            while left<right:
                sum=sorted_arr[left]+sorted_arr[right]
                if sum == target:
                    ans.append([sorted_arr[i],sorted_arr[left],sorted_arr[right]])
                    left=left+1
                    right=right-1
                    while left<n and sorted_arr[left] == sorted_arr[left-1]:
                        left=left+1
                    while right>=0 and  sorted_arr[right]==sorted_arr[right+1]:
                         right=right-1
                elif sum > target:
                    right=right-1
                else:
                    left=left+1
        return ans



        