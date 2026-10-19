class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n=len(nums)
        maxdiff=float("inf")
        sorted_arr=sorted(nums)
        resultant_sum=0
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                sum=sorted_arr[i]+sorted_arr[left]+sorted_arr[right]
                diff=abs(sum-target)
                if diff < maxdiff:
                    maxdiff=diff
                    resultant_sum=sum
                if sum == target:
                    break
                elif sum>target:
                    right=right-1
                else:
                    left=left+1
        return resultant_sum
                