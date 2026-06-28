class Solution:
    def reverse_arr(self,nums,low,high):
        while low<high:
           nums[low],nums[high]=nums[high],nums[low]
           low+=1
           high-=1

    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%len(nums)
        self.reverse_arr(nums,n-k,n-1)
        self.reverse_arr(nums,0,n-k-1)
        self.reverse_arr(nums,0,n-1)
        return nums

        