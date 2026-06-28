class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum=[nums[0]]
        count=0
        freq={}
        for i in range(1,len(nums)):
            prefixSum.append(prefixSum[i-1]+nums[i])
        
        for i in range(len(prefixSum)):

            if prefixSum[i] == k:
                count+=1
            
            rem=prefixSum[i]-k

            if rem in freq:
                count += freq[rem]

            if prefixSum[i] in freq:
                freq[prefixSum[i]] += 1
            else:
                freq[prefixSum[i]] = 1
            
             
        return count

             

            