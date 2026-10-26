class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        low=0
        high=0
        n=len(nums)
        result=float("-inf")
        freq={}
        while high < n:
             char=nums[high]
             freq[char]=freq.get(char,0)+1
             lenght=high-low+1
             lenght_of_one = freq.get(1, 0)
             diff=lenght-lenght_of_one
             while diff > k:
                freq[nums[low]]-=1
                low=low+1
                lenght=high-low+1
                lenght_of_one = freq.get(1, 0)
                diff=lenght-lenght_of_one
            

             result=max(result,lenght)
             high=high+1
             if high == n:
                break
        return result            