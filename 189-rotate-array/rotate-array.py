class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        if k>=len(nums):
            k=k%len(nums)
        nums[:]=nums[n-k:n]+nums[0:n-k]
        return nums
        