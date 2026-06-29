class Solution:
    def maxPower(self, nums: str) -> int:
        max_power=1
        count=0
        start=0
        for i in range(len(nums)):
            if nums[start] == nums[i]:
                count+=1
                max_power=max(max_power,count)
            else:
                start=i
                count=1
        return max_power

        